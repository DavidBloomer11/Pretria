import requests
import random
import json

class ElectronicPatientFileConnector():
    '''This class is a connector class to a dummy API that is used to access patient healthrecords
    The health records aren't real, but it simulates the possibility
    '''
    def __init__(self):
        self.url = 'https://randomuser.me/api/'        

    def get_patient(self,citizen_service_number:str):
        '''This logic simulates the logic of accesing a patient file from an API.
            Normally it takes citizen service  number as input and returns patient file.
            
            Returns a dictionary object with the following information:
                - first_name
                - last_name
                - gender
        '''
        # Choose random nationality
        NATIONALITIES = ['gb','nl','fr']

        response = requests.get(
            url = self.url + '?nat=' + random.choice(NATIONALITIES)
        )

        #Check for error
        if response.status_code == 200:
            
            patient_response = json.loads(response.content)['results'][0]

            
            first_name = patient_response['name']['first']
            last_name = patient_response['name']['last']
            gender = patient_response['gender']

            patient = {
                'first_name' : first_name,
                'last_name' : last_name,
                'gender' : gender,

            }


            return patient
        else:
            raise ValueError('Invalid request')
    
