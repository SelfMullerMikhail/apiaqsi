import sys
import os
import json

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_dir)

import requests



class Slips:
    def __init__(self, API) -> None:
        self.HEADERS = API

    def slips_index(self, BeginDate:str, Operation:str=None, Search:str=None,
                    BeginAmount:str=None, EndAmount:str=None, EndDate:str=None,
                    Devices:list=None, Cashiers:list=None, pageSize:int=None,
                    page:int=None, sorted:list=None) -> json:
        """ 
        Getting a list of slips.
        
        :param "filtered.Operation" "string"
            Possible values: purchase, void, refund, purchasewithcashback
        :param "filtered.Search" "string"
            Search string (search by slip number or transaction RRN)
        :param "filtered.BeginAmount" "string"
            Minimum amount
        :param "filtered.EndAmount" "string"
            Maximum amount
        :param "filtered.BeginDate" "required string <date-time>"
            Start date (format: YYYY-MM-DDTHH-MM-SS)
        :param "filtered.EndDate" "string <date-time>"
            End date (format: YYYY-MM-DDTHH-MM-SS)
        :param "filtered.Devices" "Array of integers <int32>"
            Array of device IDs
        :param "filtered.Cashiers" "Array of strings <uuid>"
            Array of cashier IDs
        :param "pageSize" "integer <int32> [1..100]"
            Default: 25
            Number of receipts per page. Default: 25. Limits: 1-100.
        :param "page" "integer <int32>"
            Default: 0
            Page number. Default: 0.
        :param "sorted" "Array of objects (NebularApi.Models.LkService.Sorting)"
            Sorting parameters. Default: [{ id: 'createdAt', desc: false }].
            (Array of objects (NebularApi.Models.LkService.Sorting)) 
        
        :return: Response object of the GET request to get a list of slips.
        """
        params = {
            "filtered": {
            "Operation": Operation,
            "Search": Search,
            "BeginAmount": BeginAmount,
            "EndAmount": EndAmount,
            "BeginDate": BeginDate,
            "EndDate": EndDate,
            "Devices": Devices,
            "Cashiers": Cashiers
            },
            "pageSize": pageSize,
            "page": page,
            "sorted": sorted
            }
        
        url_api = "https://api.aqsi.ru/pub/v2/Slips"
        return requests.get(url_api, headers=self.__HEADERS, params=params)