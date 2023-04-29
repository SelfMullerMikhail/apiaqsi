import sys
import os
import requests

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_dir)

from aqsi_types.aqsi_types import *
from functions.aqsi_functions import AqsiFunctions


class ClientsAqsi:
    def __init__(self, API):
        self.__HEADERS = API
    
    def clients_create(self, 
                    id:str,
                    group_id:str,
                    fio:str=None,
                    gender:int=None,
                    inn:str=None,
                    birthDate:str=None,
                    mainPhone:str=None,
                    email:str=None,
                    comment:str=None,
                    passport:str=None,
                    docType:int=None,
                    nationality:str=None,
                    address:str=None) -> json:
        """
        Creating a client for an external system
        
        :param "id": "string",
        :param "fio": "string",
        :param "group": {},
        :param "gender": 0,
        :param "inn": "string",
        :param "birthDate": "2023-04-22T13:15:49Z",
        :param "mainPhone": "string",
        :param "email": "string",
        :param "comment": "string",
        :param "passport": "string",
        :param "docType": 0,
        :param "nationality": "str",
        :param "address": "string"
        
        :return: Response object of the POST request to create a client for
            an external system.
        
        """
        pre_body = {
                "id": id,
                "fio": fio,
                "group": {"id":group_id},
                "gender": gender,
                "inn": inn,
                "birthDate": birthDate,
                "mainPhone": mainPhone,
                "email": email,
                "comment": comment,
                "passport": passport,
                "docType": docType,
                "nationality": nationality,
                "address": address
                }
        url_api = "https://api.aqsi.ru/pub/v2/Clients"
        body = AqsiFunctions.body_filter(pre_body)
        return requests.post(url_api, headers=self.__HEADERS, json=body)
        
    def clients_read(self, clientId:str) -> json:
        """
        Get customer data for an external system.
        
        :param clientId: (string) Client ID. 
        
        :return: Response object of the GET request to get customer data for
            an external system.
        """
        url_api = f"https://api.aqsi.ru/pub/v2/Clients/{clientId}"
        return requests.get(url_api, headers=self.__HEADERS)
        
    def clients_update(self, clientId:str, group_id:str, fio:str=None,
                    gender:int=None, inn:str=None, birthDate:str=None,
                    mainPhone:str=None, additionalPhone:str=None,
                    email:str=None, comment:str=None, passport:str=None,
                    docType:int=None, nationality:str=None,
                    address:str=None) -> json:
        """
        :param "group": {},
        :param "fio": "Ivanov Ivan",
        :param "gender": 1,
        :param "inn": "123124125126",
        :param "birthDate": "1970-01-01T00:00:00.0000000+00:00",
        :param "mainPhone": "88005553535",
        :param "additionalPhone": null,
        :param "email": "ivanov@example.com",
        :param "comment": "Keep tips",
        :param "passport": "4608999777",
        :param "docType": null,
        :param "nationality": null,
        :param "address": null
        
        :return: Response object of the PUT request to update customer data
            for an external system.
        """
        pre_body = {
                "group": {"id":group_id},
                "fio": fio,
                "gender": gender,
                "inn": inn,
                "birthDate": birthDate,
                "mainPhone": mainPhone,
                "additionalPhone": additionalPhone,
                "email": email,
                "comment": comment,
                "passport": passport,
                "docType": docType,
                "nationality": nationality,
                "address": address
                }
        body = AqsiFunctions.body_filter(pre_body)
        url_api = f"https://api.aqsi.ru/pub/v2/Clients/{clientId}"
        return requests.put(url_api, headers=self.__HEADERS, json=body)
        
    def clients_delete(self, clientId:str) -> json:
        """
        Deletion of a client in an external system.
        
        :param clientId: (string) Client ID. 
        
        :return: Response object of the DELETE request to
        """
        url_api = f"https://api.aqsi.ru/pub/v2/Clients/{clientId}"
        return requests.delete(url_api, headers=self.__HEADERS)