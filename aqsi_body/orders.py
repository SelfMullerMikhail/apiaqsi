import sys
import os
import datetime as dt
import requests

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_dir)

from aqsi_types.aqsi_types import *
from headers_function import get_header




class OrdersAqsi:
    def __init__(self, STRIPE_SECRET_KEY:str) -> None:
        self.__HEADERS = get_header(STRIPE_SECRET_KEY)
    
    def orders_index(self, 
                    filtered_DateFrom:str=(datetime.date.today() - datetime.
                    timedelta(days=1))
                    .strftime("%Y-%m-%dT%H-%M"),
                    pageSize:int=None,
                    page:int=None,
                    sorted:QasiSorted=None,
                    filtered_Search:str=None,
                    filtered_Clients:list=None,
                    filtered_BeginAmount:str=None,
                    filtered_EndAmount:str=None,
                    filtered_DateTo:str=None,
                    filtered_Status:str=None) -> dict:
        """ 
        Getting a list of deferred orders.
        

        :param "pageSize" "25"
        :param "page" "0"
        :param "sorted" "Array of objects (NebularApi.Models.LkService.Sorting)"
        :param "filtered.Search" "string"
        :param "filtered.Clients" "Array of strings <uuid>"
        :param "filtered.BeginAmount" "string"
        :param "filtered.EndAmount" "string"
        :param "filtered.DateFrom" "required string (example parameter: 
            filtered.DateFrom=2021-03-01T12-00)"
        :param "filtered.DateTo" "string"
        :param "filtered.Status" "Array of strings (example: a request
            "?filtered.Status[0]=Paid&filtered.Status[1]=Cancelled&filtered.
                status[2]=Partially Paid"
            will return a list of orders with statuses: Paid, Cancelled, 
                Partially Paid)"
        
        :return: Response object of the GET request to get a list 
            of deferred orders.
            
        """
        params = {
            "pageSize": pageSize,
            "page": page,
            "sorted": sorted,
            "filtered.Search": filtered_Search,
            "filtered.Clients": filtered_Clients,
            "filtered.BeginAmount": filtered_BeginAmount,
            "filtered.EndAmount": filtered_EndAmount,
            "filtered.DateFrom": filtered_DateFrom,
            "filtered.DateTo": filtered_DateTo,
            "filtered.Status": filtered_Status,
            }
        url_api = "https://api.aqsi.ru/pub/v2/Orders"
        return requests.get(url_api, headers=self.__HEADERS, params=params)
        
    def orders_create(self, 
                    id:str,
                    number:str,
                    content:ContentOrder=None,
                    dateTime =  f"{dt.datetime.now().isoformat()}",
                    device:str=None,
                    shop:str=None,
                    cashier:str=None,
                    clientId:str=None,
                    comment:str=None,
                    deliveryAddress:str=None,
                    pickAddress:str=None,
                    status:str=None,
                    cancellationReason:str=None,
                    isEditableByDevice:bool=None,
                    ignoreItemCodeCheck:bool=None) -> dict:
        """ 
        Creating and updating a deferred order.
        
        :param "id": "stringId",
        :param "number": "OderNumber",
        :param "dateTime": "2019-08-14T12:15:43.0000000+00:00",
        :param "device": null,
        :param "shop": null,
        :param "cashier": null,
        :param "clientId": null,
        :param "comment": null,
        :param "deliveryAddress": null,
        :param "pickAddress": null,
        :param "status": null,
        :param "cancellationReason": null,
        :param "content": {},
        :param "isEditableByDevice": false,
        :param "ignoreItemCodeCheck": false
        
        :return: Response object of the POST request to create and update a 
            deferred order.
        """
        
        url_api = "https://api.aqsi.ru/pub/v2/Orders/simple"
        body = {
                "id": id,
                "number": number,
                "dateTime": dateTime,
                "device": device,
                "shop": shop,
                "cashier": cashier,
                "clientId": clientId,
                "comment": comment,
                "deliveryAddress": deliveryAddress,
                "pickAddress": pickAddress,
                "status": status,
                "cancellationReason": cancellationReason,
                "content": content,
                "isEditableByDevice": isEditableByDevice,
                "ignoreItemCodeCheck": ignoreItemCodeCheck
                }
        # body = json.dumps(pre_body)
        return requests.post(url_api, headers=self.__HEADERS, json=body)
        
    def orders_read(self, orderId:str):
        """ 
        Fetching information about a deferred order by its external id.
        
        :param orderId: (string) Order ID. 
        
        :return: Response object of the GET request to fetch information 
            about a deferred order by its external id.
        """
        url_api = f"https://api.aqsi.ru/pub/v2/Orders/simple/{orderId}"
        return requests.get(url_api, headers=self.__HEADERS)
        
    def orders_delete(self, orderId:str):
        """Delete Deferred Order by its externalId. The method accepts an
        externalId parameter that was used to create this order in the 
            external system.
        
        :param orderId: (string) Order ID. 
        
        :return: Response object of the DELETE request to delete a
            deferred order.
        """
        url_api = f"https://api.aqsi.ru/pub/v2/Orders/simple/{orderId}"
        return requests.delete(url_api, headers=self.__HEADERS)