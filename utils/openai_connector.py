from pydantic import BaseModel
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from utils.pydantic_models import AdditionalQuestions, TriageUrgency, DifferentialDiagnosis

class OpenAiChatConnector:
    #Constructor
    def __init__(self,
                    model_configuration = {},
                    model="gpt-3.5-turbo",
                    temperature=0.4,
                    max_tokens=1024,
                    system_description = '',
                    top_p = 1.0,
                    frequency_penalty = 0,
                    presence_penalty = 0,
                    api_key: str = None
                    ):
        '''Initializes the configuration for the model. model_configuration is a dictionary object containing the configuration data'''
        
        #Model
        if model_configuration.get('model'):
            self.model = model_configuration['model']
        else:
            self.model = model
        
        #Temperature
        if model_configuration.get('temperature'):
            self.temperature = model_configuration['temperature']
        else:
            self.temperature = temperature
        #Max tokens
        if model_configuration.get('max_tokens'):
            self.max_tokens = model_configuration['max_tokens']
        else:
            self.max_tokens = max_tokens
        
        #System description
        if model_configuration.get('system_description'):
            self.system_description = model_configuration['system_description']
        else:
            self.system_description = system_description
        
        #Top p
        if model_configuration.get('top_p'):
            self.top_p = model_configuration['top_p']
        else:
            self.top_p = top_p
        
        #frequency_penalty
        if model_configuration.get('frequency_penalty'):
            self.frequency_penalty = model_configuration['frequency_penalty']
        else:
            self.frequency_penalty = frequency_penalty

        #presence_penalty
        if model_configuration.get('presence_penalty'):
            self.presence_penalty = model_configuration['presence_penalty']
        else:
            self.presence_penalty = presence_penalty

        #API key
        self.api_key = api_key

    def get_additional_questions(self, description:str, age:str,gender):
        '''Gets 10 additional questions based on the description
        Uses Langchain instead of OpenAI as the previous version fucked up a bit.
        
        '''
        message = f"{description} | Patient age: {str(age)} | Patient gender {gender}"

        data = self._perform_chat_completion(message, AdditionalQuestions)

        
        if not data["is_related_to_medical"]:
            raise ValueError("The input is not related to medical symptoms.")

        lst = []
        # Loop through the questions and output types
        for i in range(1, 11):
            try:
                question = data[f"question_{i}"]
                output_type = data[f"output_type_{i}"]
                
                lst.append({'question': question, 'answer_type': output_type})
            except KeyError:
                pass

        return lst

    def get_urgency(self, description:str, gender:str, age:int, question_list_string: str) -> int:
        '''Returns the urgnecy of a case based on some inputs.\n
        The urgency is a number between 1 and 5 with 1 being most urgent and 5 least.
        '''

        message = f'{description} | Patient {str(age)} years old, gender {gender} | Answers to questions: {question_list_string}'


        response = self._perform_chat_completion(message, TriageUrgency)
        return response['urgency']

    def get_differential_diagnosis(self,description:str,age:int,gender:str,question_list_string : str):
        '''Returns a list of diagnoses with likelihood based on some inputs.
        Questionliststring should be a string in the form of "Q1:A1; Q2:A2; Q...:A...
        '''
        message = f'{description} | Patient {age} years old, gender {gender} | Answers to questions: {question_list_string}'

        response = self._perform_chat_completion(message, DifferentialDiagnosis)

        # Reformat the response
        lst = []
        for i in range(1, 11):
            try:
                disease = response[f"disease_{i}"]
                likelihood = response[f"likelihood_{i}"]
                
                lst.append({'disease': disease, 'likelihood': int(likelihood)})
            except KeyError:
                pass

        return lst
  

    def _perform_chat_completion(
            self, 
            message : str,
            structured_output_class : BaseModel
            ):
        '''Performs a chat completion based on the message provided.'''
        llm = ChatOpenAI(
            model=self.model,
            api_key=self.api_key,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=self.top_p,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty
        )

        structured_llm = llm.with_structured_output(structured_output_class)

        messages = [
            SystemMessage(self.system_description),
            HumanMessage(message)
        ]

        response = structured_llm.invoke(messages)
        
        return response.dict()
        
