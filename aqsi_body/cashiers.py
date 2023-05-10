import sys
import os
import requests

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_dir)

from aqsi_types.aqsi_types import *
from functions.aqsi_functions import AqsiFunctions
from headers_function import get_header




class CashiersAqsi():
    def __init__(self, STRIPE_SECRET_KEY:str) -> None:
        self.__HEADERS = get_header(STRIPE_SECRET_KEY)
        
    def get_CustomProperties(self, *args, **kwargs):
        return CustomProperties(*args, **kwargs)

    def cashiers_create(self,
                        name:str,
                        position:str,
                        inn:str=None,
                        pin:str=None,
                        code:str=None,
                        devices:list=None,
                        img:AqsiImg=None,
                        externalId:str=None,
                        shops:list=None,
                        customProperties:CustomProperties=None):
        
        """Creating a cashier for an external system.
        
        :param name ex: 'Mihail'
        :param position ex: 'Cashier'/'Admin'
        :param inn: '000000000000'
        :param pin ex: '2231'
        :param code: 
        :param devices ex: ["123", "32gw3FG3g3434g3", 334]
        :example: "devices": [4, 47]
        :param externalId ex: '1k23o3kk'
        :param shops: None
        
        :return: Response object of the POST request to create a cashier.
        """
        url_api = "https://api.aqsi.ru/pub/v2/Cashiers"
        pre_body = {
        "name": name,
        "inn": inn,
        "position": position,
        "pin": pin,
        "code": code,
        "devices": devices,
        "img": img,
        "externalId": externalId,
        "shops": shops,
        "customProperties": customProperties
        }
        body = AqsiFunctions.body_filter(pre_body)
        return requests.post(url_api, headers=self.__HEADERS, json=body)
        
    def cashiers_read(self, cashierId:str) -> dict:
        """
        Getting information about a specific cashier by their identifier in the
        external system.
        
        :param cashierId: (string) Cashier identifier in the external system. 
        
        :return: A dictionary containing the cashier information.
        """
        url_api = f"https://api.aqsi.ru/pub/v2/Cashiers/{cashierId}"
        return requests.get(url_api, headers=self.__HEADERS)
        
    def cashiers_update_PUT(self, cashierId:str, name:str, position:str,
                            inn:AqsiImg=None, pin:str=None, code:str=None,
                            devices:list=None, img:object=None,
                            externalId:str=None, shops:list=None,
                            customProperties:list = None) -> dict:
        """
        Updating a cashier for an external system.
        
            :param name ex: 'Mihail'
        :param position ex: 'Cashier'/'Admin'
        :param inn: '000000000000'
        :param pin ex: '2231'
        :param code: 
        :param devices ex: ["123", "32gw3FG3g3434g3", 334]
        :example: "devices": [4, 47]
        :param externalId ex: '1k23o3kk'
        :param shops: None
        
        :return: Response object of the PUT request to update a cashier.
        """
        url_api = f"https://api.aqsi.ru/pub/v2/Cashiers/{cashierId}"
        pre_body = {
                "name": name,
                "inn": inn,
                "position": position,
                "pin": pin,
                "code": code,
                "devices": devices,
                "img": img,
                "externalId": externalId,
                "shops": shops,
                "customProperties": customProperties
                }
        body = AqsiFunctions.body_filter(pre_body)
        return requests.put(url_api, headers=self.__HEADERS, json=body)
        
    def cashiers_update_POST(self, cashierId:str, name:str, position:str,
                            inn:str=None, pin:str=None, code:str=None,
                            devices:list=None, img:AqsiImg=None,
                            externalId:str=None, shops:list=None,
                            customProperties:list = None) -> dict:
        """
        Update cashier for external system.
        
        :param name ex: 'Mihail'
        :param position ex: 'Cashier'/'Admin'
        :param inn: '000000000000'
        :param pin ex: '2231'
        :param code: 
        :param devices ex: ["123", "32gw3FG3g3434g3", 334]
        :example: "devices": [4, 47]
        :param externalId ex: '1k23o3kk'
        :param shops: None
                                        
        :return: Response object of the PUT request to update a cashier.
        """
        url_api = f"https://api.aqsi.ru/pub/v2/Cashiers/{cashierId}"
        pre_body = {
                "name": name,
                "inn": inn,
                "position": position,
                "pin": pin,
                "code": code,
                "devices": devices,
                "img": img,
                "externalId": externalId,
                "shops": shops,
                "customProperties": customProperties
                }
        body = AqsiFunctions.body_filter(pre_body)
        return requests.post(url_api, headers=self.__HEADERS, json=body)
        
    def cashiers_delete(self, cashierId:str) -> dict:
        """
        Delete a cashier in an external system.
        
        :param cashierId: (string) Cashier identifier in the external system. 
        
        :return: Response object of the DELETE request to delete a cashier.
        """
        url_api = f"https://api.aqsi.ru/pub/v2/Cashiers/{cashierId}"
        return requests.delete(url_api, headers=self.__HEADERS)
        
    def cashiers_index(self) -> dict:
        """
        Getting a list of cashiers for an external system.
        
        :return: Response object of the GET request to get a list of cashiers.
        """
        url_api = "https://api.aqsi.ru/pub/v2/Cashiers/list"
        return requests.get(url_api, headers=self.__HEADERS)