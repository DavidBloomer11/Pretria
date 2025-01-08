from utils.openai_connector import OpenAiChatConnector
from triage.models import Encounter, EncounterQuestion, EncounterDiseasePrediction, Patient, OpenAIModelConfiguration
from.serializers import OpenAIModelConfigurationSerializer
from django.shortcuts import get_object_or_404
from django.conf import settings

API_KEY = settings.OPENAI_API_KEY


class EncounterController():
    def __init__(self, uuid : str):
        '''Constructor method takes a uuid as an argument'''
        try:
            self.encounter = Encounter.objects.get(uuid = uuid)

        except Encounter.DoesNotExist as e:
            raise e

    def __perform_error_check__(self):
        '''Method that should be called before each controller method that performs error checks'''
        if self.encounter.gender == None:
            raise ValueError('Encounter has no gender given')
        elif self.encounter.description == None:
            raise ValueError('Encounter has no description given')
        elif self.encounter.age == None:
            raise ValueError('Encounter has no age given')
        
    def generate_questions(self):
        '''Controller that generates additional questions for the patients using OpenAI's model'''
        self.__perform_error_check__()

        obj = OpenAIModelConfiguration.get_latest_model('additional_questions')

        #Initialize connector with latest model configuration by passing serialized data (in dictionary form)
        connector = OpenAiChatConnector(
            model_configuration=OpenAIModelConfigurationSerializer(obj).data,
            api_key=API_KEY
            
            )

        question_list = connector.get_additional_questions(
                description= self.encounter.description,
                age= self.encounter.age,
                gender= self.encounter.gender
            )

        # Save questions
        for question in question_list:
            q = EncounterQuestion()
            q.encounter = self.encounter
            q.question = question['question']
            q.answer_type = question['answer_type']
            q.save()
            question['id'] = q.pk
            

        return question_list

    def generate_triage(self):
        '''Controller function that handles the generation of a triage prediction'''
        self.__perform_error_check__()

        obj = OpenAIModelConfiguration.get_latest_model('triage')
        connector = OpenAiChatConnector(
            model_configuration=OpenAIModelConfigurationSerializer(obj).data,
            api_key=API_KEY
            )
        
        urgency = connector.get_urgency(
            description=self.encounter.description,
            gender = self.encounter.gender,
            age=self.encounter.age,
            question_list_string= EncounterQuestion.create_string_list(self.encounter)
        )
        
        #Save urgency
        self.encounter.urgency_prediction = urgency
        self.encounter.save()

        if urgency == 1 or urgency == 2:
            triage_class = 1
            triage_description = 'Visit emergency department.'
        elif urgency == 3 or urgency == 4:
            triage_class = 2
            triage_description = 'Visit your local after-hour care center.'
        else:
            triage_class = 3
            triage_description = 'You can wait until normal hours to go your general practicioner.'

        response = {
            'urgency' : urgency,
            'triage_class' : triage_class,
            'triage_description' : triage_description,
            'follow_up_code' : self.encounter.follow_up_code
        }

        return response

    def generate_differential_diagnosis(self):
        '''Controller function that handles the generation of a differential diagnosis'''
        self.__perform_error_check__()

        #Check if differential diagnosis has allready been generated, is needed because every API call costs money
        if EncounterDiseasePrediction.check_for_predictions(self.encounter) == True:
            raise ValueError('Encounter allready has a disease prediction')

        #Initialize connector with latest model configuration by passing serialized data (in dictionary form)
        obj = OpenAIModelConfiguration.get_latest_model('differential_diagnosis')
        connector = OpenAiChatConnector(
            model_configuration=OpenAIModelConfigurationSerializer(obj).data,
            api_key=API_KEY
            )


        # Get differential diagnosis via OpenAI api
        differential_diagnoses = connector.get_differential_diagnosis(
            gender= self.encounter.gender,
            description=self.encounter.description,
            age=self.encounter.age,
            question_list_string= EncounterQuestion.create_string_list(self.encounter)
        )

        #Save predictions to database
        EncounterDiseasePrediction.save_disease_prediction_list(
            disease_prediction_list=differential_diagnoses,
            encounter=self.encounter
        )

        return differential_diagnoses

    def register_patient(self, citizen_service_number:str) -> Encounter:
        '''Registers a patient to an encounter'''

        if self.encounter.patient != None:
            raise ValueError('Encounter has allready registered a patient')

    	#Check if patient allready exists in database
        patient = Patient.get_or_create_patient(citizen_service_number)
        self.encounter.patient = patient
        self.encounter.save()

        return self.encounter

