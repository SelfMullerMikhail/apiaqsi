import sys
import os
import requests
import pickle

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_dir)

from functions.aqsi_functions import AqsiFunctions
from headers_function import get_header
from aqsi_types.aqsi_types import *



class GoodsAqsi:
    def __init__(self, STRIPE_SECRET_KEY:str) -> None:
        self.__HEADERS = get_header(STRIPE_SECRET_KEY)
        
    def goods_create(self, id:str, group_id:str, tax:int, unit:str, subject:int,
                    name:str, payment_method_type:int, type:str="simple", 
                    production_cost:float=None, margin_percent:float=None,
                    is_weight:int=None, unit_code:int=None, 
                    is_orderable:bool=None, slot_info:SlotinfoGoods=None,
                    sku:str=None, ic_sku:str=None, price:float=None, 
                    barcodes:list=None, img:object=None,
                    last_purchase_price:float=None, accounting_method:str=None,
                    cooking_time_minutes:int=None,
                    cooking_time_seconds:int=None, cooking_receipt:str=None,
                    non_tradable:bool=None, marking_type:int=None,
                    min_price:float=None, custom_properties:list=None,
                    receipt_properties:object=None,
                    max_discount_percent:int=None, nomenclature_code:str=None,
                    industry_attribute:object=None, no_return:int=None)-> dict:
        """
        Creating a product in a personal account by account identifier, the response returns 
        the time of placing the message in the data bus queue.
        
        :param "id": "string",
        :param "group_id": "string",
        :param "type": "simple",
        :param "productionCost": 0,
        :param "marginPercent": 0,
        :param "isWeight": 0,
        :param "tax": 1,
        :param "unit": "string",
        :param "unitCode": 0,
        :param "subject": 1,
        :param "isOrderable": false,
        :param "name": "string",
        :param "slotInfo": {},
        :param "sku": "string",
        :param "1cSku": "string",
        :param "price": 0,
        :param "barcodes": [],
        :param "img": {},
        :param "lastPurchasePrice": 0,
        :param "accountingMethod": "string",
        :param "cookingTimeMinutes": 0,
        :param "cookingTimeSeconds": 0,
        :param "cookingReceipt": "string",
        :param "nonTradable": false,
        :param "markingType": 1,
        :param "minPrice": 0,
        :param "customProperties": [],
        :param "paymentMethodType": 1,
        :param "receiptProperties": {},
        :param "maxDiscountPercent": 0,
        :param "nomenclatureCode": "string",
        :param "industryAttribute": {},
        :param "noReturn": 0
        
        :param :return: Response object of the POST request to create a product.
        """
        url_api = "https://api.aqsi.ru/pub/v2/Goods"
        pre_body = {
            "id": id,
            "group_id": group_id,
            "type": type,
            "productionCost": production_cost,
            "marginPercent": margin_percent,
            "isWeight": is_weight,
            "tax": tax,
            "unit": unit,
            "unitCode": unit_code,
            "subject": subject,
            "isOrderable": is_orderable,
            "name": name,
            "slotInfo": slot_info,
            "sku": sku,
            "1cSku": ic_sku,
            "price": price,
            "barcodes": barcodes,
            "img": img,
            "lastPurchasePrice": last_purchase_price,
            "accountingMethod": accounting_method,
            "cookingTimeMinutes": cooking_time_minutes,
            "cookingTimeSeconds": cooking_time_seconds,
            "cookingReceipt": cooking_receipt,
            "nonTradable": non_tradable,
            "markingType": marking_type,
            "minPrice": min_price,
            "customProperties": custom_properties,
            "paymentMethodType": payment_method_type,
            "receiptProperties": receipt_properties,
            "maxDiscountPercent": max_discount_percent,
            "nomenclatureCode": nomenclature_code,
            "industryAttribute": industry_attribute,
            "noReturn": no_return
            }
        body = AqsiFunctions.body_filter(pre_body)
        return requests.post(url_api, headers=self.__HEADERS, json=body)
        
        
        
    def goods_update(self, id:str, groupId:str, type:str, tax:int, unit:str,
                    subject:int, name:str, paymentMethodType:int,
                    productionCost:float=None, marginPercent:float=None,
                    isWeight:int=None, unitCode:int=None, 
                    isOrderable:bool=None, slotInfo:object=None, sku:str=None,
                    IcSku:str=None, price:float=None,  barcodes:list=None,
                    img:AqsiImg=None, lastPurchasePrice:float=None,
                    accountingMethod:str=None, cookingTimeMinutes:int=None,
                    cookingTimeSeconds:int=None, cookingReceipt:str=None,
                    nonTradable:bool=None, markingType:int=None,
                    minPrice:float=None, customProperties:CustomProperties=None,
                    receiptProperties:ReceiptPropertiesGoods=None,
                    maxDiscountPercent:int=None, nomenclatureCode:str=None,
                    industryAttribute:object=None, noReturn:int=None):
        """
        Updating a product in the personal account in the context of the
        account, the response returns the 
        time of putting the message in the data bus queue.
        
        :param "id": "string",
        :param "group_id": "string",
        :param "type": "simple",
        :param "productionCost": 0,
        :param "marginPercent": 0,
        :param "isWeight": 0,
        :param "tax": 1,
        :param "unit": "string",
        :param "unitCode": 0,
        :param "subject": 1,
        :param "isOrderable": false,
        :param "name": "string",
        :param "slotInfo": {},
        :param "sku": "string",
        :param "1cSku": "string",
        :param "price": 0,
        :param "barcodes": [],
        :param "img": {},
        :param "lastPurchasePrice": 0,
        :param "accountingMethod": "string",
        :param "cookingTimeMinutes": 0,
        :param "cookingTimeSeconds": 0,
        :param "cookingReceipt": "string",
        :param "nonTradable": false,
        :param "markingType": 1,
        :param "minPrice": 0,
        :param "customProperties": [],
        :param "paymentMethodType": 1,
        :param "receiptProperties": {},
        :param "maxDiscountPercent": 0,
        :param "nomenclatureCode": "string",
        :param "industryAttribute": {},
        :param "noReturn": 0
        :return: Response object of the PUT request to create a product.
        """
        
        pre_body = {
                "id": id,
                "group_id": groupId,
                "type": type,
                "productionCost": productionCost,
                "marginPercent": marginPercent,
                "isWeight": isWeight,
                "tax": tax,
                "unit": unit,
                "unitCode": unitCode,
                "subject": subject,
                "isOrderable": isOrderable,
                "name": name,
                "slotInfo": slotInfo,
                "sku": sku,
                "1cSku": IcSku,
                "price": price,
                "barcodes": barcodes,
                "img": img,
                "lastPurchasePrice": lastPurchasePrice,
                "accountingMethod": accountingMethod,
                "cookingTimeMinutes": cookingTimeMinutes,
                "cookingTimeSeconds": cookingTimeSeconds,
                "cookingReceipt": cookingReceipt,
                "nonTradable": nonTradable,
                "markingType": markingType,
                "minPrice": minPrice,
                "customProperties": customProperties,
                "paymentMethodType": paymentMethodType,
                "receiptProperties": receiptProperties,
                "maxDiscountPercent": maxDiscountPercent,
                "nomenclatureCode": nomenclatureCode,
                "industryAttribute": industryAttribute,
                "noReturn": noReturn
                }
        url_api = "https://api.aqsi.ru/pub/v2/Goods"
        body = AqsiFunctions.body_filter(pre_body)
        return requests.put(url_api, headers=self.__HEADERS, json=body)
        
    def goods_read(self, goodId:str) -> dict:
        """
        Get a product from the personal account in the context of the account
        
        :param goodId: (string) Product identifier in the external system. 
        
        :return: Response object of the GET request to get a product.
        """
        url_api = f"https://api.aqsi.ru/pub/v2/Goods/{goodId}"
        return requests.get(url_api, headers=self.__HEADERS)
        
    def goods_delete(self, goodId:str) -> dict:
        """
        Deletion of a product in the personal account within the account scope,
        the response returns the time of the message placement in the data bus.
        
        :param goodId: (string) Product identifier in the external system. 
        :return: Response object of the DELETE request to delete a product.
        """
        url_api = f"https://api.aqsi.ru/pub/v2/Goods/{goodId}"
        return requests.delete(url_api, headers=self.__HEADERS)
        
    def goods_index(self, pageNumber:int=None, group_id:str=None) -> dict:
        """
        This phrase can be translated as "Getting a list of products from
        a personal account in the context of an account."
        
        :pram "rows": [],
        :pram "pages": 1

        :return: Response object of the GET request to get a list of products.
        """
        url_api = "https://api.aqsi.ru/pub/v2/Goods/list"
        params = {'pageNumber': pageNumber,
                    'group_id': group_id} 
        
        return  requests.get(url_api, headers=self.__HEADERS, params=params)
        
    def goods_set_price(self, shops:ProductsGoods) -> dict:
        """
        Setting prices for goods and associating them with stores.
        
        :param: shops
        
        :return: Response object of the POST request to set prices for goods.
        """
        url_api = "https://api.aqsi.ru/pub/v2/Goods/prices"

        return requests.post(url_api, headers=self.__HEADERS, json=shops)
        
    def goods_bulk_upsert(self, file:BulkUpsertGoods) -> dict:
        """
        Sending a GZip archive of goods, the response returns the time of 
        placing the message in the queue on the data bus. The archived file
        should contain a JSON consisting of the payload, removeObsolete, and
        nonAtomic fields. removeObsolete is a boolean indicating the need to
        remove entity objects not listed in the payload field, with a default
        value of false. nonAtomic is a boolean indicating the need to process
        the elements of the payload array separately, with a default value of
        false. payload is an array of structures corresponding to the entity 
        model, ExtendedGoodDto.
        
        :param file:
        
        :return: Response object of the POST request to send a GZip 
            archive of goods.
        """
        url_api = "https://api.aqsi.ru/pub/v2/ListGoods"
        files = {'file': ('filename', pickle.dumps(file), 'multipart/form-data')}
        return requests.post(url_api, headers=self.__HEADERS, files=files)
        
        
    def goods_bulk_upsert_status(self, guid:str) -> dict:
        """
        Getting the upload status of a batch of goods messages by identifier
        
        :param guid: (string <uuid>) Message identifier. 
        
        :return: Response object of the GET request to get the upload status 
            of a batch of goods messages by identifier.
        """
        url_api = f"https://api.aqsi.ru/pub/v2/ListGoods/{guid}/status"
        return requests.get(url_api, headers=self.__HEADERS)