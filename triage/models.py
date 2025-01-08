import secrets
import string
import uuid
from datetime import datetime, timedelta

from django.db import models
from django.utils import timezone

from dashboard.models import Doctor, MedicalPractice
from utils.bioportal import BioPortalConnector
from utils.electronic_patient_file import ElectronicPatientFileConnector
from utils.metamaplite import MetaMapLiteConnector
from django.conf import settings

BIO_PORTAL_API_KEY = settings.BIO_PORTAL_API_KEY

# Create your models here.
class Disease(models.Model):
    disease_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    snomed_ct = models.CharField(max_length=12,null=True)
    icpc2p = models.CharField(max_length=12,null=True)
    icd10 = models.CharField(max_length=12,null=True)
    cui = models.CharField(max_length=12,null=True)

    class Meta:
        managed = True
        db_table = 'Disease'

    def __str__(self):
        return self.name
    
    def get_or_create_disease(disease:str):
        '''Input is the string name of a disease. 
        If the disease allready exists in the database it will return the object.
        If not, it will create a new entry
        '''
        queryset = Disease.objects.filter(name = disease)
        if queryset.exists():
            #Disease allready exists
            return queryset.first()
        else:
            #Disease doesn't exist, create new one
            cui = MetaMapLiteConnector().get_cui(disease)
            mapping = BioPortalConnector(BIO_PORTAL_API_KEY).get_mapping_by_cui(cui)

            new_disease = Disease(
                name=disease,
                snomed_ct = mapping.get('snomed_ct'),
                cui = cui,
                icpc2p = mapping.get('icpc2p'),
                icd10 = mapping.get('icd10')
            )
            new_disease.save()
            return new_disease

class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    citizen_service_number = models.CharField(max_length=15)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(choices=[('male','Male'),('female','Female')], max_length=6)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, null=True)

    def get_or_create_patient(citizen_service_number:str):
        '''Returns a patient object if its citizen service number allready exists in the database, 
        otherwise creates a new patient via Electronic Patient File API and returns the object'''
        queryset = Patient.objects.filter(citizen_service_number=citizen_service_number)
        if queryset.exists():
            return queryset.first()
        else:
            #Create new patient
            connector = ElectronicPatientFileConnector()
            try:
                patient = connector.get_patient(citizen_service_number)
                
                new_patient = Patient(
                    first_name = patient['first_name'],
                    last_name = patient['last_name'],
                    gender = patient['gender'],
                    citizen_service_number = citizen_service_number
                )
                new_patient.save()
                return new_patient
            except Exception as e:
                raise ValueError(e)

class Encounter(models.Model):
    GENDER_CHOICES = [('male','Male'),('female','Female')]

    def generate_code():
        alphabet = string.ascii_letters + string.digits  # defines the alphabet of characters to choose from
        code = ''.join(secrets.choice(alphabet) for i in range(8))  # generates an 8-character code
        return code.upper()
    

    #Properties
    encounter_id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    follow_up_code = models.CharField(default=generate_code, max_length=8)
    urgency_prediction = models.IntegerField(max_length=1, null=True, blank=True)
    timestamp = models.DateTimeField(auto_created=True, auto_now=True)
    description = models.CharField(max_length=1000, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE, null=True)


    def __str__(self):
        return str(self.timestamp)

    class Meta:
        managed = True
        db_table = 'Encounter'

class EncounterQuestion(models.Model):
    encounter_question_id = models.AutoField(primary_key=True)
    encounter = models.ForeignKey(Encounter, models.CASCADE)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=200)
    answer_type = models.CharField(max_length=10)

    def __str__(self):
        return 'Encounter: ' + str(self.encounter.pk) + ': ' + self.question

    def create_string_list(encounter: Encounter):
        string = ''
        question_list = EncounterQuestion.objects.filter(encounter=encounter)
        count = 0
        for q in question_list:
            string += str(count) + '. ' + q.question + ': ' + q.answer + ';'
        return string

    class Meta:
        managed = True
        db_table = 'EncounterQuestion'

class Consultation(models.Model):
    #Meta information
    consultation_id = models.AutoField(primary_key=True)
    encounter = models.ForeignKey(Encounter, models.CASCADE)
    datetime_registered = models.DateTimeField(auto_created=True, auto_now=True)
    datetime_start_consultation = models.DateTimeField(auto_created=False, auto_now=False, null=True, blank=True)
    datetime_end_consultation = models.DateTimeField(auto_created=False, auto_now=False, null=True, blank=True)
    medical_practice = models.ForeignKey(MedicalPractice, on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(Doctor,on_delete=models.SET_NULL,null=True, blank=True)

    #Clinical examination data
    hearthrate = models.IntegerField(max_length=3,null=True,blank=True)
    temperature = models.FloatField(max_length=3,null=True,blank=True)
    saturation = models.IntegerField(max_length=3,null=True,blank=True)
    blood_pressure_systolic = models.IntegerField(max_length=3,null=True,blank=True)
    blood_pressure_diastolic = models.IntegerField(max_length=3,null=True,blank=True)
    weight = models.FloatField(max_length=6,null=True,blank=True)
    length = models.IntegerField(max_length=3,null=True,blank=True)
    objective = models.TextField(null=True,blank=True)

    #Anamnesis
    subjective = models.TextField(null=True,blank=True)

    #Urgency
    actual_urgency = models.IntegerField(max_length=1,null=True,blank=True)

    #Disease
    actual_disease = models.ForeignKey(Disease, models.SET_NULL, null=True, blank=True)
    
    class Meta:
        managed = True
        db_table = 'Consultation'

    def register_consultation(follow_up_code : str, medical_practice : int):
        '''Register a consultation for a patient at a particular medical practice using the follow up follow_up_code'''
        #Check if follow_up_code exists
        encounter_list = Encounter.objects.filter(follow_up_code = follow_up_code.upper())

        if encounter_list.exists():
            encounter = encounter_list.last()
            #Check if patient is registered
            if Consultation.objects.filter(encounter=encounter).exists():
                raise ValueError('Patient allready registered.')
            else:
                consultation = Consultation(encounter=encounter, medical_practice=MedicalPractice.objects.get(pk=int(medical_practice)))
                consultation.save()
                return consultation
                

        else:
            raise ValueError(f'Encounter with follow-up code {follow_up_code} does not exist.')

    def get_number_of_consultations(medical_practice: int, date_start:datetime, date_end:datetime) -> int:
        '''Returns the number of consultations for a certain medical practice within a certain timeframe.
        '''
        start_time = datetime.combine(date_start, datetime.min.time())
        end_time = datetime.combine(date_end, datetime.max.time())

        return Consultation.objects.filter(
            medical_practice=medical_practice,
            datetime_registered__gte=start_time,
            datetime_registered__lte=end_time
        ).count()
    
    def get_number_in_waiting_room(medical_practice: int) -> int:
        yesterday = timezone.now().date() - timedelta(days=1)


        return Consultation.objects.filter(
            datetime_registered__gte=yesterday,
            datetime_start_consultation = None
        ).count()
    
    def get_waiting_room(medical_practice: int) -> models.QuerySet:
        '''Returns a queryset of registered consultations that are currently in the waiting room from a particular medical practice. \n
        Also includes a possible disease for each patient'''
        # Take yesterday as time registered: this will prevent people staying in the waiting room for ever.
        yesterday = timezone.now().date() - timedelta(days=1)
        queryset = Consultation.objects.filter(
            datetime_registered__gte=yesterday,
            datetime_start_consultation = None
        ).order_by('datetime_registered')

        for consultation in queryset:
            qs = EncounterDiseasePrediction.get_disease_list(consultation.encounter)
            consultation.disease_list = qs
        return queryset
    
    def get_average_consultation_time():
        # Get all consultations
        consultations = Consultation.objects.all()

        total_duration = timedelta(seconds=0,minutes=0)
        total_consultations = 0

        # Calculate total duration
        for consultation in consultations:
            if consultation.datetime_start_consultation and consultation.datetime_end_consultation:
                duration = consultation.datetime_end_consultation - consultation.datetime_start_consultation
                total_duration += duration
                total_consultations += 1
                

        # Calculate average duration
        if total_consultations > 0:
            average_duration = total_duration / total_consultations

            return average_duration
        else:
            return None
        
class EncounterDiseasePrediction(models.Model):
    encounter_diagnosis_prediction_id = models.AutoField(primary_key=True)
    encounter = models.ForeignKey(Encounter, models.CASCADE)
    disease = models.ForeignKey(Disease, models.CASCADE)
    likelihood = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'EncounterDiseasePrediction'

    def save_disease_prediction_list(disease_prediction_list:list, encounter:Encounter):
        '''Method that saves differnetial diagnosis predictions for a particular encounter
        Input is a list containing {'disease': D, 'likelihood': L}
        '''
        count = 1
        for element in disease_prediction_list:
            print(count)
            disease = element['disease']
            likelihood = element['likelihood']

            obj = EncounterDiseasePrediction(
                encounter=encounter,
                disease=Disease.get_or_create_disease(disease),
                likelihood=likelihood
            )
            obj.save()
            count+=1

    def check_for_predictions(encounter:Encounter):
        '''Checks wether an encounter allready has a disease prediction or not.
        If yes, it will return True; if no, it will return False
        '''
        if EncounterDiseasePrediction.objects.filter(encounter=encounter).exists():
            return True
        else:
            return False
        
    def get_disease_list(encounter : Encounter):
        '''Returns the diseaselist for a particular encounter in descending order (highest likelihood first)'''
        return EncounterDiseasePrediction.objects.filter(encounter=encounter).order_by('-likelihood')
    


class OpenAIModelConfiguration(models.Model):
    CHOICES = [
        ('triage','Triage'),
        ('differential_diagnosis','Differential diagnosis'),
        ('additional_questions','Additional questions'),
        ('other','Other')
        ]

    model_type = models.CharField(choices=CHOICES,null=False, blank=False, max_length=50)
    active = models.BooleanField(default=False, null=False)
    datetime_created = models.DateTimeField(auto_created=True)
    datetime_active_since = models.DateTimeField(auto_created=True, null=True, blank=True)

    #Open AI paramameters
    model = models.CharField(max_length=50, null=False)
    temperature = models.FloatField(default=0.0, null=False, max_length=3)
    max_tokens = models.IntegerField(null=False, default=256)
    top_p = models.FloatField(max_length=3, default=1.0, null=False)
    frequency_penalty = models.FloatField(max_length=3, default=0.0)
    presence_penalty = models.FloatField(max_length=3, default=0.0)
    system_description = models.TextField(default='',blank=True)


    def save(self, *args, **kwargs):
        if self.active and not self.datetime_active_since:
            self.datetime_active_since = timezone.now()
        
        if self.active == False and self.datetime_active_since != None:
            self.datetime_active_since = None

        super().save(*args, **kwargs)

    def __str__(self):
        if self.active:
            return self.model_type + ' | ' + str(self.datetime_created) +' | active'
        else:
            return self.model_type + ' | ' + str(self.datetime_created) +' | inactive'


    def get_latest_model(model_type:str):
        '''Returns latest active model configuration for a particular model type.
        If none exists, or if no model is active, it will return an error. \n
        Available model types: \n
            - differential_diagnosis
            - additional_questions
            - triage
        '''
        queryset = OpenAIModelConfiguration.objects.filter(model_type = model_type, active = True)

        if queryset.exists():
            model_configuration = queryset.first()
            return model_configuration
        else:
            raise ValueError('There is no active model configuration for this model type')




