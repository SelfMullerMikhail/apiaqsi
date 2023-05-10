import sys
import os

import requests

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_dir)

from functions.aqsi_functions import AqsiFunctions
from headers_function import get_header
from aqsi_types.aqsi_types import *


class GoodsCategoryAqsi:
    def __init__(self, STRIPE_SECRET_KEY:str) -> None:
        self.__HEADERS = get_header(STRIPE_SECRET_KEY)
        
    def goodsCategory_create(self, id:str, name:str, defaultSubject:int, 
                            defaultTax:int, defaultPaymentMethodType:int,
                            defaultMarkingType:int=None, number:int=None,
                            parent:str=None, defaultUnit:str=None,
                            defaultUnitCode:int=None,
                            customProperties:CustomProperties=None) -> json:
        """Creating a category in the personal account within 
        the scope of the account, the response includes the 
        time of placing the message in the data bus queue.

        param: "id": "7f541f4f-9031-4d4f-b752-df11c1ba3c2e",
        param: "name": "Abricot",
        param: "number": 5,
        param: "parent": "00000000-0000-0000-0000-000000000000",
        param: "defaultSubject": 11,
        param: "defaultTax": 6,
        param: "defaultUnit": "kg",
        param: "defaultUnitCode": null,
        param: "defaultMarkingType": null,
        param: "customProperties": null,
        param: "defaultPaymentMethodType": 4
            
        :return: Response object of the POST request to create a category.
        """
        url_api = "https://api.aqsi.ru/pub/v2/GoodsCategory"
        body = {
            "id": id,
            "name": name,
            "number": number,
            "parent": parent,
            "defaultSubject": defaultSubject,
            "defaultTax": defaultTax,
            "defaultUnit": defaultUnit,
            "defaultUnitCode": defaultUnitCode,
            "defaultMarkingType": defaultMarkingType,
            "customProperties": customProperties,
            "defaultPaymentMethodType": defaultPaymentMethodType
            }
        body = AqsiFunctions.body_filter(body)
        return requests.post(url_api, headers=self.__HEADERS, json=body)
        
    def goodsCategory_update(self, id:str, name:str, defaultSubject:int,
                            defaultTax:int, defaultPaymentMethodType:int,
                            defaultMarkingType:int=None, number:int=None,
                            parent:str=None, defaultUnit:str=None,
                            defaultUnitCode:int=None,
                            customProperties:CustomProperties=None) -> json:
        """Updating a category in the personal account within 
        
        :param "id": "string",
        :param "name": "string",
        :param "number": 0,
        :param "parent": "string",
        :param "defaultSubject": 1,
        :param "defaultTax": 1,
        :param "defaultUnit": "string",
        :param "defaultUnitCode": 0,
        :param "defaultMarkingType": 1,
        :param "customProperties": [],
        :param "defaultPaymentMethodType": 1

        :return: Response object of the PUT request to uppdate a category.
        """
        
        url_api = "https://api.aqsi.ru/pub/v2/GoodsCategory"
        body = {
            "id": id,
            "name": name,
            "number": number,
            "parent": parent,
            "defaultSubject": defaultSubject,
            "defaultTax": defaultTax,
            "defaultUnit": defaultUnit,
            "defaultUnitCode": defaultUnitCode,
            "defaultMarkingType": defaultMarkingType,
            "customProperties": customProperties,
            "defaultPaymentMethodType": defaultPaymentMethodType
            }
        body = AqsiFunctions.body_filter(body)
        return requests.put(url_api, headers=self.__HEADERS, json=body)
        
    def goodsCategory_delete(self, 
                            categoryId:str) -> json:
        """
        Deleting a category in the personal account within the account scope,
        with the response including the message queuing time on the data bus. 
        
        :param categoryId: (string) Category identifier in the external system. 
        
        return: Response object of the DELETE request to delete a category.
        """
        url_api = f"https://api.aqsi.ru/pub/v2/GoodsCategory/{categoryId}"
        return requests.delete(url_api,
                            headers=self.__HEADERS)
        
    def goodsCategory_index(self) -> json:
        """
        Getting a list of product categories in the context of the account.

        :return: Response object of the GET request to get a list of product
            categories.
        """
        url_api = "https://api.aqsi.ru/pub/v2/GoodsCategory/list"
        return requests.get(url_api, headers=self.__HEADERS)
        
    def goodsCategory_bulk_upsert(self,
                                file:ListGoodsCategories) -> json:
        """
        Sending a GZip archive of categories, in response, the time of placing 
        a message on the data bus is returned. The archived file should contain
        Json, consisting of fields payload, removeObsolete and nonAtomic.
        RemoveObsolete - bool (indicates the need to delete entity objects not 
        listed in the payload field. The default value is false). nonAtomic - 
        bool (indicates the need to process the elements of the payload
        array separately. The default value is false). payload - 
        GoodCategoryDto[] (an array of structures that correspond to the 
        entity model).
        
        :return: Response object of the POST request to send a GZip archive 
            of categories.
        """
        url_api = "https://api.aqsi.ru/pub/v2/ListGoodsCategories"
        return requests.post(url_api, headers=self.__HEADERS,
                            data=str(file).encode("UTF-8"))
        
    def goodsCategory_bulk_upsert_status(self, guid:str) -> json:
        """
        Getting the status of a batch of messages uploaded for categories by ID
        
        :param guid: (string <uuid>) Message ID. 
        
        :return: Response object of the GET request to get the status of a
            batch of messages 
                uploaded for categories by ID.
        """
        url_api = f"https://api.aqsi.ru/pub/v2/ListGoodsCategories/{guid}/status"
        return requests.get(url_api, headers=self.__HEADERS)
    
    # 
