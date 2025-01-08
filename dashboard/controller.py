from triage.models import Consultation, Patient, Disease
import datetime


class ConsultationController():
    def __init__(self):
        pass

    def register_consultation(self, follow_up_code:str, citizen_service_number:str, medical_practice:int):
        '''Registers the consultation for a patient upon arrival at a medical practice'''
        #Check if there is a follow up code / citizen service number given
        if follow_up_code == None:
            raise ValueError('No follow up code given.')
        if citizen_service_number == None:
            raise ValueError('No citizen service number given.')

        #Create/get patient file
        patient = Patient.get_or_create_patient(citizen_service_number)

        #Register consultation
        consultation = Consultation.register_consultation(follow_up_code, medical_practice)
        consultation.encounter.patient = patient
        consultation.encounter.save()
        

        return consultation
    
        

    def perform_consultation(self,data:dict, consultation: Consultation):

        #Subjective
        subjective = data.get('subjective')
        consultation.subjective = subjective

        #Temperature
        temperature = data.get('temperature')
        try:
            consultation.temperature = int(temperature)
        except:
            pass
        #hearthrate
        hearthrate = data.get('hearthrate')
        try:
            consultation.hearthrate = float(hearthrate)
        except:
            pass
        #saturation
        saturation = data.get('saturation')
        try:
            consultation.saturation = int(saturation)
        except:
            pass
        #blood_pressure_systolic
        blood_pressure_systolic = data.get('blood_pressure_systolic')
        try:
            consultation.blood_pressure_systolic = int(blood_pressure_systolic)
        except:
            pass
        #blood_pressure_diastolic
        blood_pressure_diastolic = data.get('blood_pressure_diastolic')
        try:
            consultation.blood_pressure_diastolic = int(blood_pressure_diastolic)
        except:
            pass
        #weight
        weight = data.get('weight')
        try:
            consultation.weight = float(weight)
        except:
            pass
        #length
        length = data.get('length')
        try:
            consultation.length = int(length)
        except:
            pass

        
        consultation.objective = data.get('objective')

        try: consultation.actual_disease = Disease.objects.get(pk=int(data.get('disease'))) 
        except: pass

        try: consultation.actual_urgency = int(data.get('urgency'))
        except: pass

        # Set end time
        consultation.datetime_end_consultation = datetime.datetime.now()

        consultation.save()








