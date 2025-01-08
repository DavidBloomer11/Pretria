"""
MetamapLiteConnector class to connect to the MetaMapLite API and get the CUI of a given text.

MetamapLite is a tool that maps text to concepts in the Unified Medical Language System (UMLS) Metathesaurus.

No API key is required to access the MetaMapLite API.
"""


import requests

class MetaMapLiteConnector():
    def __init__(self):
        self.url = 'https://ii.nlm.nih.gov/metamaplite/rest/annotate'
        self.resultformat = 'json'
        self.acceptformat = 'text/plain'
        self.docformat = 'freetext'
        self.semantic_types = ['bact','bhvr','dsyn','inpo','lbtr','virs','sosy','patf','mobd']

    def get_cui(self, text):
        response = self.__perform_request__(text)
        try:
            #Check if CUI exists
            cui = response.json()[0]['evlist'][0]['conceptinfo']['cui']
            return cui
        except:
            return False

    
    def __perform_request__(self,input):
        headers = {'Accept' : self.acceptformat}
        payload = [('inputtext', input), ('docformat', self.docformat), ('resultformat', self.resultformat), ('sourceString', 'all'),('semanticTypeString', self.semantic_types)]

        return requests.post(self.url, payload, headers=headers)
    

