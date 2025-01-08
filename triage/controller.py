from .models import Encounter, Consultation, EncounterQuestion, EncounterDiseasePrediction, Disease
from utils.openai_connector import OpenAiChatConnector
from utils.bioportal import BioPortalConnector
from utils.metamaplite import MetaMapLiteConnector
'''
Depreciated code

def primary_symptom_controller(age,query,gender):
    connector = OpenAiChatConnector()
    response = connector.get_additional_questions(query, age, gender)

    if response == False:
        #No symptoms asked,
        return False
    else:
        #Create encounter
        encounter = Encounter(age=age ,gender=gender,description = query)
        encounter.save()
        #Create additional questions
        for item in response:
            EncounterQuestion(encounter = encounter, question=item['question'],answer_type=item['answer_type']).save()

        return encounter.uuid

def triage_prediction_controller(encounter):
    connector = OpenAiChatConnector(temperature=0.2)
    response = connector.get_differential_diagnosis(encounter.description,encounter.age,question_list=EncounterQuestion.create_string_list(encounter))

    if response == False:
        return False
    else:
        #Save differential diagnosis
        for item in response:
            #Create disease
            if Disease.objects.filter(name = item['disease']).exists():
                disease = Disease.objects.filter(name = item['disease']).last()
            else:
                #Try and fetch SNOMED etc
                mm = MetaMapLiteConnector()
                cui = mm.get_cui(item['disease'])
                
                bp = BioPortalConnector()
                mapping = bp.get_mapping_by_cui(cui)


                disease = Disease(
                    name = item['disease'],
                    icpc2p = mapping.get('icpc2p'),
                    icd10 = mapping.get('icd10'),
                    cui = cui,
                    snomed_ct = mapping.get('snomed_ct')
                    )
                disease.save()


            prediction = EncounterDiseasePrediction(encounter = encounter,disease=disease, likelihood = item['likelihood'])
            prediction.save()
        
        return True 
    

'''