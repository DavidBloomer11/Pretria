"""
This module provides a connector to the BioPortal API for retrieving mappings of medical codes 
such as SNOMED CT, ICPC2P, and ICD10 using a Concept Unique Identifier (CUI).
Classes:
    BioPortalConnector: A class to interact with the BioPortal API.
Usage:
    To use this module, create an instance of the BioPortalConnector class with your BioPortal API key.
    Then, call the `get_mapping_by_cui` method with a CUI to retrieve the corresponding mappings.
Example:
    connector = BioPortalConnector(api_key='your_api_key')
    mappings = connector.get_mapping_by_cui('C0004238')
    print(mappings)  # Output: {'snomed_ct': '123456', 'icd10': 'A01', 'icpc2p': 'B02'}

Requires API key from BioPortal to access the API.
Can be obtained by registering at https://bioportal.bioontology.org.
"""


import requests


class BioPortalConnector():
    def __init__(self, api_key = ''):
        self.api_key = api_key
        self.url = 'http://data.bioontology.org/search'
        self.ontologies = ['SNOMEDCT','ICPC2P','ICD10','ICD10CM']

    def get_mapping_by_cui(self,cui):
        '''Returns mapping of SNOMEDCT, ICPC2P and ICD10 using cui'''
        ontologies_text = ''
        for i in self.ontologies:
            ontologies_text += i + ','

        params = [('cui',cui),('apikey',self.api_key),('format','json'),('ontologies',ontologies_text)]

        response = requests.get(
            url=self.url,
            params=params
        )
        mapping = {}
        try:
            for i in response.json()['collection']:
                id = i['@id']
                if 'SNOMEDCT' in id:
                    #extract SNOMED code
                    if mapping.get('snomed_ct') == None:
                        mapping['snomed_ct'] = id.split('/')[-1]
                elif 'ICD10' in id:
                    #Extract IDC10 code
                    if mapping.get('icd10') == None:
                        mapping['icd10'] = id.split('/')[-1]
                elif 'ICPC2P' in id:
                    #Extract ICPC2 code
                    if mapping.get('icpc2p') == None:
                        mapping['icpc2p'] = id.split('/')[-1]

            return mapping
        except:
            #If it doesn't work, just return mapping
            return mapping
    





