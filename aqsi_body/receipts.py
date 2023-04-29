import sys
import os
import requests

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_dir)

from aqsi_types.aqsi_types import *


class ReceiptsAqsi:
    def __init__(self, API):
        self.__HEADERS = API
    
    def get_QasiSorted(*args, **kwargs):
        return QasiSorted(*args, **kwargs)

    def receipts_index(self,
                    BeginDate:str = (datetime.date.today() - datetime.
                    timedelta(days=1))
                    .strftime("%Y-%m-%dT%H-%M"),
                    Operation:int=None,
                    Search:str=None,
                    Order:str=None,
                    Client:str=None,
                    Shops:list=None,
                    Fd:str=None,
                    Fp:str=None,
                    ProductName:str=None,
                    BeginAmount:str=None,
                    EndAmount:str=None,
                    EndDate:str=None,
                    Devices:list=None, 
                    Cashiers:list=None,
                    pageSize:int=None,
                    page:int=None,
                    sorted:QasiSorted=None) -> dict:
        """
        Getting a list of receipts.
        
        :param filtered.Operation "1, 2, 3, 4" (NebularApi.Models.LkService.
            ReceiptTypeEnum)
        :param filtered.Search str: "search query"
        :param filtered.Order str <uuid>: "order identifier"
        :param filtered.Client str <uuid>: "client identifier"
        :param filtered.Shops list[int]: "array of store identifiers"
        :param filtered.Fd str: "FD"
        :param filtered.Fp str: "FP"
        :param filtered.ProductName str: "product name"
        :param filtered.BeginAmount str: "amount from"
        :param filtered.EndAmount str: "amount to"
        :param filtered.BeginDate str <date-time>: "beginning of period in 
            format: YYYY-MM-DDTHH-MM-SS"
        :param filtered.EndDate str <date-time>: "end of period in format: 
            YYYY-MM-DDTHH-MM-SS"
        :param filtered.Devices list[int]: "array of device identifiers"
        :param filtered.Cashiers list[str <uuid>]: "array of cashier 
            identifiers"
        :param pageSize int: "number of receipts per page, default 25 (1-100)"
        :param page int: "page number, default 0"
        :param sorted list[obj]: "sorting parameters, default: [{ id: 
            'createdAt', desc: false }]"
        
        :return: Response object of the GET request to get a list of receipts.
        """
        
        params = {
                "filtered.Operation": Operation,
                "filtered.Search": Search,
                "filtered.Order": Order,
                "filtered.Client": Client,
                "filtered.Shops": Shops,
                "filtered.Fd": Fd,
                "filtered.Fp": Fp,
                "filtered.ProductName": ProductName,
                "filtered.BeginAmount": BeginAmount,
                "filtered.EndAmount": EndAmount,
                "filtered.BeginDate": BeginDate,
                "filtered.EndDate": EndDate,
                "filtered.Devices": Devices,
                "filtered.Cashiers": Cashiers,
                "page": page,
                "pageSize": pageSize,
                "sorted": sorted
        }
        url_api = "https://api.aqsi.ru/pub/v2/Receipts"
        return requests.get(url_api, headers=self.__HEADERS, params=params)