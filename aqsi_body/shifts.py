import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_dir)

import requests




class ShiftsAqsi:
    def __init__(self, API):
        self.__HEADERS = API

    def shifts_index(self,
                    BeginDate:str,
                    pageSize:int=None,
                    page:int=None,
                    Search:str=None,
                    EndDate:str=None,
                    Shops:list=None,
                    Devices:list=None) -> dict:
        """ 
        Getting a list of shifts.
        
        :param pageSize: integer <int32> [1..100]. The number of receipts per
            
                page. Default value: 25. Limitations: 1-100.
        :param page: integer <int32>. The page number. Default value: 0.
        :param filtered.Search: string. Search string (search by shift number).
        :param filtered.BeginDate: required. string <date-time>. Start period 
            (format: YYYY-MM-DDTHH:MM:SS).
        :param filtered.EndDate: string <date-time>. End period (format:
            YYYY-MM-DDTHH:MM:SS).
        :param filtered.Shops: Array of integers <int32>. An array of shop 
            identifiers.
        :param filtered.Devices: Array of integers <int32>. An array of device
            identifiers.
        
        :return: Response object of the GET request to get a list of shifts.
        
        """
        params = {
            "pageSize": pageSize,
            "page": page, 
            "filtered.Search": Search,
            "filtered.BeginDate": BeginDate,
            "filtered.EndDate": EndDate,
            "filtered.Shops": Shops,
            "filtered.Devices": Devices
            }
        
        url_api = "https://api.aqsi.ru/pub/v2/Shifts"
        return requests.get(url_api, headers=self.__HEADERS, params=params)
        