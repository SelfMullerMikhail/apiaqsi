import sys
import os
import json
import requests

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_dir)

from functions.aqsi_functions import AqsiFunctions
from aqsi_types.aqsi_types import *



class ShopsAqsi:
    def __init__(self, API:str):
        self.__HEADERS = API

    def shops_set_price_status(self, guid: str) -> json:
        """Obtaining the status of batch message upload by identifier.

        :param guid: (string <uuid>) A string representing the unique
        identifier of the batch message upload.

        :return: A dictionary containing the status of the batch message upload.
        """
        url = f"https://api.aqsi.ru/pub/v1/ShopsPrices/{guid}/status"
        return requests.get(url, headers=self.__HEADERS)

    def shops_update(
        self,
        shopId: str,
        name: str,
        address: ShopsAddresse = None,
        url: str = None,
        longitude: str = None,
        latitude: str = None,
        onlineStore: bool = None,
        type_id: dict = None,
        customProperties: CustomProperties = None,
    ) -> json:
        """
        Update an existing shop by ID.

        :param "name": "Magic market",
        :param "address": {},
        :param "url": null,
        :param "longitude": null,
        :param "latitude": null,
        :param "onlineStore": true,
        :param "type": {},
        :param "customProperties": nullperties:
        
        :return: Response object of the PUT request to update the shop.
        """

        url_api = f"https://api.aqsi.ru/pub/v2/Shops/{shopId}"
        pre_body = {
            "name": name,
            "address": address,
            "url": url,
            "longitude": longitude,
            "latitude": latitude,
            "onlineStore": onlineStore,
            "type": type_id,
            "customProperties": customProperties,
        }
        body = AqsiFunctions.body_filter(pre_body)
        return requests.put(url_api, headers=self.__HEADERS, json=body)

    def shops_delete(self, shopId: str) -> json:
        """Deletion of a store in an external system
        
        :param shopId: (string) ID of the shop to delete.
        
        :return: Response object of the DELETE request to delete the shop.
        """
        url_api = f"https://api.aqsi.ru/pub/v2/Shops/{shopId}"
        return requests.delete(url_api, headers=self.__HEADERS)

    def shops_index(self) -> json:
        """Obtaining a list of stores in an external system

        :return: A dictionary containing the list of stores.
        """
        url_api = "https://api.aqsi.ru/pub/v2/Shops/list"
        return requests.get(url_api, headers=self.__HEADERS)

    def shops_set_price(self, file: ShopsPrices) -> json:
        """
        Sending a GZip archive of goods, in response the time of placing the
        message on the data bus queue is returned. The archived file should
        contain Json, consisting of the fields: payload - PostSetShopPrices[]
        (an array of structures corresponding to the entity model) nonAtomic -
        bool Indicates whether to process the payload array elements
        separately. In case of an error for one of the records (for example,
        the product is not found in the database), the operation is not
        terminated with an error, but this error is added to the array of
        errors, and all entities for which no errors occurred were successfully
        updated. (The default value is false.)

        :param file: (string <binary>) A string containing the JSON body.

        :return: A dictionary containing the response data from the external.
        """
        url_api = "https://api.aqsi.ru/pub/v2/ShopsPrices"
        return requests.post(url_api, headers=self.__HEADERS,
                            data=str(file).encode("UTF-8"))

    def shops_create(
        self,
        id: str,
        name: str,
        url: str = None,
        longitude: str = None,
        latitude: str = None,
        onlineStore: bool = True,
        type_id: dict = None,
        customProperties: CustomProperties = None,
        address:QasiAddress=None,
    ) -> json:
        """
        Creates a shop in the external system.

        :param id: ex = ('FRFBRW223545')
        :param name: ex = ('Magic market')
        :param address: ex = {}.
        :param url: ex = ('https//example.kek')
        :param longitude: ex = ('')
        :param latitude: ex = ('')
        :param onlineStore: ex = (True)
        :param type_id: ex = (2) Defaults to 1.
        :param customProperties: ex = ([{key:value},{key:value}])

        :return: A dictionary containing the response data from
            the external system.
        """

        url_api = "https://api.aqsi.ru/pub/v2/Shops"
        body = {
            "id": id,
            "name": name,
            "address": address,
            "url": url,
            "longitude": longitude,
            "latitude": latitude,
            "onlineStore": onlineStore,
            "type": {"id": type_id},
            "customProperties": customProperties,
        }
        return requests.post(url_api, headers=self.__HEADERS, json=body)
