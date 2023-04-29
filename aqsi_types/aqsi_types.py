import sys
import os
import base64
import json
import datetime

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_dir)

from functions.aqsi_functions import AqsiFunctions

class CustomProperties(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_properties(self, key: str, value: str):
        """
        :param key = key (str)
        :value = value (str/list/dict/int,float....)
        """
        self.append({key: value})

    def dell_properties(self, key: str):
        """
        Remove object for key
        :param keu = key (str)
        """
        for item in self:
            if key in item:
                self.remove(item)
                return True
        return False


class ShopsPrices(dict):
    def __init__(self,
                YOUR_SHOP_ID_V2: str,
                nonAtomic: bool = False):
        """
        Store address (dadata object, see 
            https://dadata.ru/api/suggest/#about-address)
        
        :param YOUR_SHOP_ID_V2 "32"
        :param nonAtomic "false"
        """
        self.goods = []
        self["nonAtomic"] = nonAtomic
        self["payload"] = [{"id": YOUR_SHOP_ID_V2, "goods": self.goods}]

    def append_good(self, id: str, price: float, maxDiscountPercent: int):
        self.goods.append(
            {"id": id, "price": price, "maxDiscountPercent": maxDiscountPercent}
        )

    def delete_good(self,
                    id: str):
        for good in self.goods:
            if good["id"] == id:
                self.goods.remove(good)
                return True
        return False

    
class ShopsAddresse(dict):
    def __init__(self,
                value:str=None,
                unrestricted_value:str=None,
                city:str=None,
                house:str=None,
                region:str=None,
                street:str=None,
                country:str=None) -> dict:
        """
        :param value ('c. Moscow, st. Kekovaya h.13')
        :param unrestricted_value (None)
        :param city ('Moscow')
        :param house ('13')
        :param region ('Moscovskaya oblast')
        :param street ('Kekovaya')
        :param country ('Russian Federation')
        """
        
        pre_body= {
        "city": city,
        "house": house,
        "region": region,
        "street": street,
        "country": country
        }
        self["data"] = AqsiFunctions.body_filter(pre_body)
        if value is not None:
            self["value"] = value
        if unrestricted_value is not None:
            self["unrestricted_value"] = unrestricted_value
        if self == {'data': {}}:
            raise Exception("You shout to write minimum 1 argument")
            

class AqsiImg(dict):
    def __init__(self,
                name:str,
                type:str,
                data:str):
        """ 
        param 'name' ex (TestName)
        :param 'data' ex (C//Admin//user//photo.png)
        :param 'type' ex ('image/png"')
        """
        self["name"] = name
        self["type"] = type
        with open(data, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            self["data"] = encoded_string
    
    
class ListGoodsCategories(dict):
    def __init__(self, 
                removeObsolete:bool=False,
                nonAtomic:bool=False)-> dict:
        """
                param: "removeObsolete": false,
                param: "nonAtomic": false,
        """
        
        self["removeObsolete"] = removeObsolete
        self["nonAtomic"] = nonAtomic
        self.listCategories = []
        self["payload"] = self.listCategories
        
    def append_categories(self,
                        id:str,
                        number:str,
                        name:str, 
                        isDefault:bool=False,
                        defaultTax:str=1,
                        defaultUnit:str='1',
                        customProperties:str=None,
                        defaultMarkingType:str=None,
                        isTransport:bool=False,
                        defaultPaymentMethodType:int=4, 
                        defaultSubject:str=1) -> json:
            """ 
            Append categori
            
            :param "id": "hdpaA8gy7Z970Ic3",
            :param "number": "hdpaA8gy7Z970Ic3",
            :param "name": "New category",
            :param "isDefault": false,
            :param "defaultTax": "1",
            :param "defaultUnit": "шт",
            :param "isTransport": false,
            :param "defaultSubject": "1",
            :param "customProperties": null,
            :param "defaultMarkingType": null,
            :param "defaultPaymentMethodType": 4
            """
            
            self.listCategories.append(
            {
            "id": id,
            "number": number,
            "name": name,
            "isDefault": isDefault,
            "defaultTax": defaultTax,
            "defaultUnit": defaultUnit,
            "isTransport": isTransport,
            "defaultSubject": defaultSubject,
            "customProperties": customProperties,
            "defaultMarkingType": defaultMarkingType,
            "defaultPaymentMethodType": defaultPaymentMethodType})
        
    def remove_category(self, id:str) -> bool:
        """
        Remove category from id
        
        :id '13'
        """
        for category in self.listCategories:
            if category.get('id') == id:
                self.listCategories.pop(self.listCategories.index(category))
                return True
        return False
    
class SlotinfoGoods(dict):
    def __init__(self, slotId = 0, isBlocked = True, maxValue=0) -> None:
        self["slotId"] =  slotId
        self["isBlocked"] = isBlocked
        self["maxValue"] =  maxValue
        
        
        """ 
        :param slotId integer <int64> Identifier of the time slot isBlocked
        :param boolean Whether this slotId is blocked maxValue
        :param number <double> Maximum value for the slot
        """
        return None
        
class ReceiptPropertiesGoods(dict):
    def __init__(self, 
                supplierINN:str=None, 
                agentType:str=None,
                additionalAttribute:str=None, 
                manufacturerCountryCode:str=None,
                customsDeclarationNumber:str=None, 
                excise:float=None) -> None:
        """
        :param "supplierInfo": {},
        :param "supplierINN": "string",
        :param "agentType": 1,
        :param "agentInfo": {},
        :param "additionalAttribute": "string",
        :param "manufacturerCountryCode": "str",
        :param "customsDeclarationNumber": "string",
        :param "excise": 0
        """
        self["supplierINN"]= supplierINN
        self["agentType"] = agentType
        self["additionalAttribute"] = additionalAttribute
        self["manufacturerCountryCode"] = manufacturerCountryCode
        self["customsDeclarationNumber"] = customsDeclarationNumber
        self["excise"] = excise
        self = AqsiFunctions.body_filter(self)
        return None
        
    def set_supplierInfo(self, name:str=None, phoneNumber:list=None) -> None:
        """
        :param name "Mikhail Muller"
        :param  phoneNumer "+79999999999"
        """
        self["supplierInfo"]["name"] = name
        self["supplierInfo"]["phoneNumbers"] = phoneNumber
        self["supplierInfo"] = AqsiFunctions.body_filter(self["supplierInfo"])
        return None
    
    def set_agentInfo(self, paymentAgentOperation:str=None,
                    paymentOperatorName:str=None,
                    paymentOperatorAddress:str=None,
                    paymentOperatorINN:str=None,
                    paymentAgentPhoneNumbers:list=None,
                    paymentTransferOperatorPhoneNumbers:list=None,
                    paymentOperatorPhoneNumbers:str=None
                    ) -> None:
        """ 
        :param "paymentTransferOperatorPhoneNumbers": [],
        :param "paymentAgentOperation": "string",
        :param "paymentAgentPhoneNumbers": [],
        :param "paymentOperatorPhoneNumbers": [],
        :param "paymentOperatorName": "string",
        :param "paymentOperatorAddress": "string",
        :param "paymentOperatorINN": "string"
        
        return None
        """
        
        self["agentInfo"]["paymentAgentOperation"] = paymentAgentOperation
        self["agentInfo"]["paymentOperatorName"] = paymentOperatorName
        self["agentInfo"]["paymentOperatorAddress"] = paymentOperatorAddress
        self["agentInfo"]["paymentOperatorINN"] = paymentOperatorINN
        self["agentInfo"]["paymentAgentPhoneNumbers"] = paymentAgentPhoneNumbers
        self["agentInfo"]["paymentTransferOperatorPhoneNumbers"] = paymentTransferOperatorPhoneNumbers
        self["agentInfo"]["paymentOperatorPhoneNumbers"] = paymentOperatorPhoneNumbers
        self["agentInfo"] = AqsiFunctions.body_filter(self["agentInfo"])
        return None
    
class ShopsGoods(list):
    def __init__(self):
        ...
    def append_shop(self, 
                    id:str,
                    price:str = None,
                    maxDiscountPercent:float = None) -> None:
        """ 
        :param id ""3242gre343
        :param price "33"
        :param maxDiscountPercent 50
        
        return None
        """
        
        shop = {
                "id": id,
                "price": price,
                "maxDiscountPercent": maxDiscountPercent
                }
        shop = AqsiFunctions.body_filter(shop)
        self.append(shop)
        return None
    
class ProductsGoods(list):
    def __init__(self):
        ...
    def append_shop(self,
                    id:str,
                    shops:ShopsGoods,
                    defaultPrice:float=None ):
        product = {
        "id": id,
        "shops": shops,
        "defaultPrice": defaultPrice
        }
        """ 
        :param id: "gre345g"
        :param shop: "fr3g34g45"
        :param defaultPrice: 33
        """
        
        product = AqsiFunctions.body_filter(product)
        self.append(product)
        return None
    
class BulkUpsertGoods(dict):
    def __init__(self,
                removeObsolete:bool=False,
                nonAtomic:bool=False) -> None:
        self["removeObsolete"] =  removeObsolete,
        self["nonAtomic"] = nonAtomic,
        self.payload = []
        self["payload"] = self.payload 
        
        """
        :param "removeObsolete": false,
        :param "nonAtomic": false,
        :param "payload": []:
        """
        
    def append_payload(self,
                    id:str,
                    name:str,
                    group_id:str,
                    price:float,
                    tax:str,
                    type_:str="simple",
                    sku:str="",
                    lcSku:str=None,
                    unit:str="1",
                    subject:str="1",
                    productionCost:int=0,
                    marginPercent:int=5,
                    lastPurchasePrice= None,
                    img:AqsiImg=None,
                    barcodes:list=[],
                    isOrderable:bool=False,
                    isWeight:int=0,
                    nonTradable:bool=False,
                    accountingMethod:str=None,
                    cookingTimeMinutes:str=None,
                    cookingTimeSeconds:str=None,
                    cookingReceipt:str=None,
                    markingType:str = None, 
                    minPrice:str = None,
                    deletedAt:str = None, 
                    createdAt = None
                    ) -> None:
                """
                    :param "id": "hdpaA8gy7Z970Ic3",
                    :param "name": "Сигареты LD BLUE OC",
                    :param "type": "simple",
                    :param "sku": "",
                    :param "1cSku": null,
                    :param "unit": "1",
                    :param "price": 10.5,
                    :param "productionCost": 10,
                    :param "marginPercent": 5,
                    :param "lastPurchasePrice": null,
                    :param "tax": "6",
                    :param "img": null,
                    :param "subject": "1",
                    :param "barcodes": [],
                    :param "isOrderable": false,
                    :param "isWeight": 0,
                    :param "nonTradable": false,
                    :param "accountingMethod": null,
                    :param "cookingTimeMinutes": null,
                    :param "cookingTimeSeconds": null,
                    :param "cookingReceipt": null,
                    :param "markingType": null,
                    :param "group_id": "64ff353a-1a10-43eb-a650-62d9566a5376",
                    :param "minPrice": null,
                    :param "createdAt": "2019-02-14T13:59:54.460Z",
                    :param "deletedAt": null
                
                return None
                """

                if createdAt is None:
                        now = datetime.datetime.utcnow()
                        createdAt = str(now.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
                info = {
                "id":id,
                "name":name, 
                "type": type_,
                "sku": sku,
                "1cSku": lcSku,
                "unit": unit,
                "price": price,
                "productionCost": productionCost,
                "marginPercent": marginPercent,
                "lastPurchasePrice": lastPurchasePrice,
                "tax": tax,
                "img": img,
                "subject": subject,
                "barcodes": barcodes,
                "isOrderable": isOrderable,
                "isWeight": isWeight,
                "nonTradable": nonTradable,
                "accountingMethod": accountingMethod,
                "cookingTimeMinutes": cookingTimeMinutes,
                "cookingTimeSeconds": cookingTimeSeconds,
                "cookingReceipt": cookingReceipt,
                "markingType": markingType,
                "group_id": group_id,
                "minPrice": minPrice,
                "createdAt": "2019-02-14T13:59:54.460Z",
                "deletedAt": deletedAt
                }
                self.payload.append(info)
                return None
                
class QasiSorted(list):
    def __init__(self):
        ...
    
    def append_sorted_param(self, id:str, desc:bool) -> None:
        """
        :param id: "gr3gr44"
        :param desc: false
        
        return None
        """
        
        param = {id:desc}
        self.append(param)
        return None
    
    def del_param(self, id:str):
        for item in self:
            if id in item:
                self.remove(item)
                return True
        return False
                

        
class PositionsContentOders(list):
    def __init__(self):
        """
        :param "discountMoney": "0",
        :param "discountPercent": "0",
        :param "type": 3,
        :param "positions": [],
        :param "checkClose": {},
        :param "customerContact": "Ivanov Ivan",
        :param "paymentAgentOperation": null,
        :param "paymentOperatorName": null,
        :param "paymentOperatorAddress": null,
        :param "paymentOperatorINN": null,
        :param "agentType": null,
        :param "paymentTransferOperatorPhoneNumbers": null,
        :param "paymentAgentPhoneNumbers": null,
        :param "paymentOperatorPhoneNumbers": null,
        :param "supplierPhoneNumbers": null,
        :param "additionalUserAttribute": null,
        :param "automatNumber": null,
        :param "settlementAddress": null,
        :param "settlementPlace": null,
        :param "additionalAttribute": null,
        :param "customer": "Ivanov Ivan",
        :param "customerINN": null,
        :param "customerInfo": null,
        :param "industryAttribute": null,
        :param "electronicCheck": null
        
        return None
        """
        
    def set_industryAttribute(self,
                            foivId:str=None,
                            causeDocumentDate:str=None,
                            causeDocumentNumber:str=None,
                            value:str=None):
        
        industryAttribute = {"foivId":foivId,
                            "causeDocumentDate":causeDocumentDate,
                            "causeDocumentNumber":causeDocumentNumber,
                            "value":value}
        industryAttribute = AqsiFunctions.body_filter(industryAttribute)
        if industryAttribute == {}:
            raise Exception("You should create minimum 1 atribute")
        self["industryAttribute"] = industryAttribute
        
    def append_agentInfo(self,
                        paymentTransferOperatorPhoneNumbers:list =None,
                        paymentAgentOperation:str=None,
                        paymentAgentPhoneNumbers:list=None,
                        paymentOperatorPhoneNumbers:list=None,
                        paymentOperatorName:list=None,
                        paymentOperatorAddress:str=None,
                        paymentOperatorINN:str=None) -> None:
        """
        :param "paymentTransferOperatorPhoneNumbers": null,
        :param "paymentAgentOperation": "payment",
        :param "paymentAgentPhoneNumbers": null,
        :param "paymentOperatorPhoneNumbers": null,
        :param "paymentOperatorName": "operatorName",
        :param "paymentOperatorAddress": "г. Москва, ул. Ленинская Слобода, 19 строение 32",
        :param "paymentOperatorINN": null
        """
        
        
        agentInfo = {
            "paymentTransferOperatorPhoneNumbers":paymentTransferOperatorPhoneNumbers,
            "paymentAgentOperation":paymentAgentOperation,
            "paymentAgentPhoneNumbers":paymentAgentPhoneNumbers,
            "paymentOperatorPhoneNumbers": paymentOperatorPhoneNumbers,
            "paymentOperatorName":paymentOperatorName,
            "paymentOperatorAddress":paymentOperatorAddress,
            "paymentOperatorINN":paymentOperatorINN}
        agentInfo = AqsiFunctions.body_filter(agentInfo)
        if agentInfo == {}:
            raise Exception("You should create minimum 1 position")
        if "agentInfo" not in self:
            self["agentInfo"] = []
        self["agentInfo"].append(agentInfo) 
        return None
        
    def append_customProperties(self, key:str, value) -> None:
        if "customProperties" not in self["customProperties"]:
            self["customProperties"] = []
        
        propertie = {"key":key, "value":value}
        self["customProperties"].append(propertie)
        return None
    
    def append_supplierInfo(self, name:str, phoneNumbers:str):
        if "supplierInfo" not in self["phoneNumbers"]:
            self["supplierInfo"] = []
        supplierInfo = {"name":name, "phoneNumbers":phoneNumbers}
        self["supplierInfo"].append(supplierInfo)
        
    def set_position(self, 
                    quantity:float,
                    price:float,
                    tax:int,
                    paymentMethodType:int,
                    paymentSubjectType:int,
                    
                    sku:str=None, 
                    id:str=None,
                    discountMoney:float=None,
                    positionId:str=None,
                    markingType:int=None,
                    nomenclatureCode:str=None,
                    itemCode:str=None,
                    soldAmount:float=None,
                    barcodes:list=None, 
                    addingType:int=None,
                    addedAt:str = f"{datetime.datetime.now().isoformat()}",
                    editable:bool=None,
                    text:str=None,
                    agentInfo=None,
                    unitOfMeasurement:str=None,
                    unitCode:int=None,
                    additionalAttribute:str=None,
                    manufacturerCountryCode:str=None,
                    customsDeclarationNumber:str=None,
                    supplierINN:str=None,
                    supplierInfo=None,
                    excise:float=None,
                    agentType=None, 
                    customProperties=None,
                    industryAttribute:dict=None,
                    noReturn:int=None,
                    discountPercent:float=None,
                    maxDiscountPercent:float=None,
                    minPrice:float=None) -> None:
        
        """
        :param "sku": "",
        :param "id": null,
        :param "discountMoney": 0,
        :param "positionId": null,
        :param "markingType": null,
        :param "nomenclatureCode": null,
        :param "itemCode": null,
        :param "soldAmount": 0,
        :param "barcodes": null,
        :param "addingType": 0,
        :param "addedAt": "2023-04-22T05:50:44.1534454+00:00",
        :param "editable": true,
        :param "quantity": 1,
        :param "price": 10,
        :param "tax": 6,
        :param "text": "Contract  №ARS15/123474",
        :param "paymentMethodType": 4,
        :param "paymentSubjectType": 4,
        :param "agentInfo": null,
        :param "unitOfMeasurement": "Piece",
        :param "unitCode": 0,
        :param "additionalAttribute": null,
        :param "manufacturerCountryCode": null,
        :param "customsDeclarationNumber": null,
        :param "supplierINN": null,
        :param "supplierInfo": null,
        :param "excise": null,
        :param "agentType": null,
        :param "customProperties": null,
        :param "industryAttribute": null,
        :param "noReturn": 0,
        :param "discountPercent": "0",
        :param "maxDiscountPercent": "0",
        :param "minPrice": "0"
        """

        position = {
            "sku": sku,
            "id": id,
            "discountMoney": discountMoney,
            "positionId": positionId,
            "markingType": markingType,
            "nomenclatureCode": nomenclatureCode,
            "itemCode": itemCode,
            "soldAmount": soldAmount,
            "barcodes": barcodes,
            "addingType": addingType,
            "addedAt": addedAt,
            "editable": editable,
            "quantity": quantity,
            "price": price,
            "tax": tax,
            "text": text,
            "paymentMethodType": paymentMethodType,
            "paymentSubjectType": paymentSubjectType,
            "agentInfo": agentInfo,
            "unitOfMeasurement": unitOfMeasurement,
            "unitCode": unitCode,
            "additionalAttribute": additionalAttribute,
            "manufacturerCountryCode": manufacturerCountryCode,
            "customsDeclarationNumber": customsDeclarationNumber,
            "supplierINN": supplierINN,
            "supplierInfo": supplierInfo,
            "excise": excise,
            "agentType": agentType,
            "customProperties": customProperties,
            "industryAttribute": industryAttribute,
            "noReturn": noReturn,
            "discountPercent": discountPercent,
            "maxDiscountPercent": maxDiscountPercent,
            "minPrice": minPrice
            }
        position = AqsiFunctions.body_filter(position)
        self=position
        
class QrPayTransactionOrders(dict):
    def __init__(self, operationId:str, orderId:str):
        self["operationId"] = operationId
        self["orderId"] = orderId
        
class ChequeOrders(list):
    def __init__(self):
        ...
    def append_cheque(self, amount:int, quantity:float, product:str=None):
        cheque = {"amount":amount, "quantity":quantity, product:product}
        cheque = AqsiFunctions.body_filter(cheque)
        self.append(cheque)
        

        
class SpasiboOrders(dict):
    def __init__(self):
        ...
    
    def set_credit(self,
                hash:str=None,
                pan4:str=None,
                slip:str=None,
                cheque:ChequeOrders=None,
                currency:str=None,
                partnerId:str=None,
                terminalId:str=None,
                amountToPay:int=None,
                dateAndTime:str=None,
                totalAmount:int=None,
                idTransaction:str=None,
                terminalLocation:str=None,
                bonuses:int=None
                ):
        credit = {"hash":hash,
                "pan4":pan4,
                "slip":slip,
                "cheque":cheque,
                "currency":currency,
                "partnerId":partnerId,
                "terminalId":terminalId,
                "amountToPay":amountToPay,
                "dateAndTime":dateAndTime,
                "totalAmount":totalAmount,
                "idTransaction":idTransaction,
                "terminalLocation":terminalLocation,
                "bonuses":bonuses}
        credit = AqsiFunctions.body_filter(credit) 
        self["credit"] = credit
        
        
    def set_debit(self,
                amountToPay:int,
                hash:str=None,
                pan4:str=None,
                slip:str=None,
                discount:ChequeOrders=None,
                cheque:ChequeOrders=None,
                currency:str=None,
                partnerId:str=None,
                terminalId:str=None,
                dateAndTime:str=None,
                totalAmount:int=None,
                idTransaction:str=None,
                terminalLocation:str=None,
                bonuses:int=None
                ):
        debit = {
                "hash":hash,
                "pan4":pan4,
                "slip":slip,
                "discount":discount,
                "cheque":cheque,
                "currency":currency,
                "partnerId":partnerId,
                "terminalId":terminalId,
                "amountToPay":amountToPay,
                "dateAndTime":dateAndTime,
                "totalAmount":totalAmount,
                "idTransaction":idTransaction,
                "terminalLocation":terminalLocation,
                "bonuses":bonuses}
        
        debit = AqsiFunctions.body_filter(debit)
        self["debit"] = debit
        
class AcquiringDataOrder(dict):
    def __init__(self,
                type_:str,
                date:str=None,
                cashierId:str=None,
                amount:float=None,
                tsi:str=None,
                rrn:str=None,
                expirationDate:str=None,
                companyName:str=None,
                customerContact:str=None,
                calculationAddress:str=None,
                errorCode:str=None,
                errorMessage:str=None,
                text:str=None,
                cardholder:str=None,
                acquirerAgentName:str=None,
                cashlessType:int=None,
                qrPayTransaction:QrPayTransactionOrders=None,
                merchantId:str=None,
                currency:str = None,
                respCode:str=None,
                id:str=None,
                acquirerBankName:str=None,
                transactionId:str=None,
                slipNumber:str=None,
                approvalCode:str=None,
                terminalId:str=None,
                spasibo:SpasiboOrders=None,
                maskPan:str=None,
                aid:str=None,
                tvr:str=None,
                apn:str=None,
                iin:str=None,
                signNeeded:bool=None
                ):
            """
            :param type: "pur
                chase", "void", "refund", "purchasewithcashback"
            :param date: string, Nullable, date of transaction
            :param cashierId: string, Nullable, cashier id
            :param amount: number, double, amount of transaction
            :param tsi: string, Nullable, TSI attribute of slip
            :param rrn: string, Nullable, attribute of slip, operation number 
                for refunds
            :param expirationDate: string, Nullable, expiration date of the 
                card
            :param companyName: string, Nullable, company name
            :param customerContact: string, Nullable, email or phone number of 
                customer
            :param calculationAddress: string, Nullable, address of 
                installation of cash register for calculations
            :param errorCode: string, Nullable, error code during payment
            :param errorMessage: string, Nullable, description of error during 
                payment
            :param text: string, Nullable, text of the slip
            :param cardholder: string, Nullable, name of the cardholder
            :param acquirerAgentName: string, Nullable, intermediary to
                acquiring bank
            :param cashlessType: integer, int32, enum: 1,2,3
            1 - Non-cash
            2 - Card
            3 - QR-code
            :param qrPayTransaction: object, Nullable, transaction when paying 
                with QR-Pay service
            :param merchantId: string, Nullable, terminal owner's ID
            :param currency: integer, int32, currency code according to ISO
                4217
            :param respCode: string, Nullable, response code during payment
            :param id: string, uuid, Nullable, slip uuid
            :param acquirerBankName: string, Nullable, bank name
            :param transactionId: string, Nullable, operation id at the bank
            :param slipNumber: string, Nullable, slip number
            :param approvalCode: string, Nullable, confirmation code
            :param terminalId: string, Nullable, terminal id
            :param spasibo: object, Nullable, "Thank you" transaction for
                payment
            :param maskPan: string, Nullable, masked card number
            :param aid: string, Nullable, AID - authorization number in the
                network
            :param tvr: string, Nullable, TVR - attribute of slip
            :param apn: string, Nullable, APN - attribute of slip. Type of a
                uthorization network (Card type)
            :param iin: string, Nullable, IIN - attribute of slip. Type of 
                MasterCard/Visa card
            :param signNeeded: boolean, whether customer signature is required
                or not
            """
            
            acquiringData = {
                "type":type_,
                "date":date,
                "cashierId":cashierId,
                "amount":amount,
                "tsi":tsi,
                "rrn":rrn,
                "expirationDate":expirationDate,
                "companyName":companyName,
                "customerContact":customerContact,
                "calculationAddress":calculationAddress,
                "errorCode":errorCode,
                "errorMessage":errorMessage,
                "text":text,
                "cardholder":cardholder,
                "acquirerAgentName":acquirerAgentName,
                "cashlessType":cashlessType,
                "qrPayTransaction:":qrPayTransaction,
                "merchantId":merchantId,
                currency:currency,
                "respCode":respCode,
                "id":id,
                "acquirerBankName":acquirerBankName,
                "transactionId":transactionId,
                "slipNumber":slipNumber,
                "approvalCode":approvalCode,
                "terminalId":terminalId,
                "spasibo":spasibo,
                "maskPan":maskPan,
                "aid":aid,
                "tvr":tvr,
                "apn":apn,
                "iin":iin,
                "signNeeded":signNeeded
            }
            acquiringData = AqsiFunctions.body_filter(acquiringData)
            self = acquiringData

class PaymentsOrder(list):
    def __init__(self):
        ...
        
    def append_payments(self, 
                    type_:int,
                    amount:float,
                    acquiringData:AcquiringDataOrder,
                    processedAt:str=None,
                    index:int=None,
                    parentIndex:int=None) -> None:
        """
        :param "acquiringData": null,
        :param "processedAt": null,
        :param "index": null,
        :param "parentIndex": null,
        :param "type": 1,
        :param "amount": 10
        
        retrun None
        """
        payment = {
            "type":type_,
            "amount":amount,
            "acquiringData":acquiringData,
            "processedAt":processedAt,
            "index":index,
            "parentIndex":parentIndex
        }
        payment = AqsiFunctions.body_filter(payment)
            
        self.append(payment)
        
class CheckCloseOrder(dict):
    def __init__(self,
                taxationSystem:int=None,
                payments:PaymentsOrder=None) -> None:
        """
        :param "payments": [],
        :param "taxationSystem": 0
        
        retrun None
        """
        if taxationSystem is not None:
            self["taxationSystem"] = taxationSystem
        if payments is not None:
            self["payments"] = payments   
        
        
class AdditionalUserAttributeOrder(dict):
    def __init__(self, name:str=None, value:str=None):
        additionalUserAttribute = {"name":name, "value":value}
        additionalUserAttribute = AqsiFunctions.body_filter(additionalUserAttribute)
        if additionalUserAttribute == {}:
            raise Exception("You should create minimum 1 argiment")
        self = additionalUserAttribute
        
class CustomerInfoOrder(dict):
    def __init__(self,
                birthDate:str=None,
                nationality:str=None,
                docType:int=None,
                passport:str=None,
                address:str=None
                ) -> None:
        customerInfo = {
                "birthDate": birthDate,
                "nationality":nationality,
                "docType": docType,
                "passport":passport,
                "address":address}
        customerInfo = AqsiFunctions.body_filter(customerInfo)
        if customerInfo == {}:
            raise Exception("YOu should create minimum 1 argument")
        self = customerInfo
        
class IndustryAttributeOrder(dict):
    def __init__(self,
                foivId:str=None,
                causeDocumentDate:str=None,
                causeDocumentNumber:str=None,
                value:str=None) -> None:
        """
        :param foivId
            string 3 characters Nullable
            Corresponds to: FFD 1.2
            FOIV identifier, 1262. Must be one of: 001, 002, 003, 004, 005, 006, 
            007, 008, 009, 010, 011, 012, 013, 014, 015, 016, 017, 018, 019, 020, 
            021, 022, 023, 024, 025, 026, 027, 028, 029, 030, 031, 032, 033, 034, 
            035, 036, 037, 038, 039, 040, 041, 042, 043, 044, 045, 046, 047, 048, 
            049, 050, 051, 052, 053, 054, 055, 056, 057, 058, 059, 060, 061, 062, 
            063, 064, 065, 066, 067, 068, 069, 070, 071, 072.
        :param causeDocumentDate string Nullable
            Corresponds to: FFD 1.2
            Cause document date (Format dd.mm.yy), 1263
        :param causeDocumentNumber
            string <= 32 characters Nullable
            Corresponds to: FFD 1.2
            Cause document number, 1264
        :param value
            string <= 256 characters Nullable
            Corresponds to: FFD 1.2
            Value of industry-specific attribute, 1265
        """
        
        industryAttribute = {
                "foivId":foivId,
                "causeDocumentDate":causeDocumentDate,
                "causeDocumentNumber":causeDocumentNumber,
                "value":value}
        industryAttribute = AqsiFunctions.body_filter(industryAttribute)
        if industryAttribute == {}:
            raise Exception("You should create minimum 1 argument")
    
class ContentOrder(dict):
    def __init__(self, 
                type_:int,
                discountMoney:float=None,
                discountPercent:float=None,
                position:PositionsContentOders=None,
                checkClose: CheckCloseOrder=None,
                customerContact:str=None,
                paymentAgentOperation:str=None,
                paymentOperatorName:str=None,
                paymentOperatorAddress:str=None,
                paymentOperatorINN:str=None,
                agentType:int=None,
                paymentTransferOperatorPhoneNumbers:list=None,
                paymentAgentPhoneNumbers:list=None,
                paymentOperatorPhoneNumbers:list=None,
                supplierPhoneNumbers:str=None,
                additionalUserAttribute:AdditionalUserAttributeOrder=None,
                automatNumber:str=None,
                settlementAddress:str=None,
                settlementPlace:str=None,
                additionalAttribute:str=None,
                customer:str=None,
                customerINN:str=None,
                customerInfo:CustomerInfoOrder=None,
                industryAttribute:IndustryAttributeOrder=None,
                electronicCheck:int=None) -> None:
        
        """
        :param "discountMoney": "0",
        :param "discountPercent": "0",
        :param "type": 3,
        :param "positions": [],
        :param "checkClose": {},
        :param "customerContact": "Иванов Иван",
        :param "paymentAgentOperation": null,
        :param "paymentOperatorName": null,
        :param "paymentOperatorAddress": null,
        :param "paymentOperatorINN": null,
        :param "agentType": null,
        :param "paymentTransferOperatorPhoneNumbers": null,
        :param "paymentAgentPhoneNumbers": null,
        :param "paymentOperatorPhoneNumbers": null,
        :param "supplierPhoneNumbers": null,
        :param "additionalUserAttribute": null,
        :param "automatNumber": null,
        :param "settlementAddress": null,
        :param "settlementPlace": null,
        :param "additionalAttribute": null,
        :param "customer": "Иванов Иван",
        :param "customerINN": null,
        :param "customerInfo": null,
        :param "industryAttribute": null,
        :param "electronicCheck": null
        
        return None
        """
        
        self.checkClose = checkClose
        self.additionalUserAttribute = additionalUserAttribute
        self.customerInfo = customerInfo
        self.industryAttribute = industryAttribute
        
        self["discountMoney"] = discountMoney
        self["discountPercent"] = discountPercent
        self["type"] = type_
        self["positions"] = position 
        self["checkClose"] = self.checkClose
        self["customerContact"] = customerContact
        self["paymentAgentOperation"] = paymentAgentOperation
        self["paymentOperatorName"] = paymentOperatorName
        self["paymentOperatorAddress"] = paymentOperatorAddress
        self["paymentOperatorINN"] = paymentOperatorINN
        self["agentType"] = agentType
        self["paymentTransferOperatorPhoneNumbers"] = paymentTransferOperatorPhoneNumbers
        self["paymentAgentPhoneNumbers"] = paymentAgentPhoneNumbers
        self["paymentOperatorPhoneNumbers"] = paymentOperatorPhoneNumbers
        self["supplierPhoneNumbers"] = supplierPhoneNumbers
        self["additionalUserAttribute"] = self.additionalUserAttribute
        self["automatNumber"] = automatNumber
        self["settlementAddress"] = settlementAddress
        self["settlementPlace"] = settlementPlace
        self["additionalAttribute"] = additionalAttribute
        self["customer"] = customer
        self["customerINN"] = customerINN
        self["customerInfo"] = self.customerInfo
        self["industryAttribute"] = self.industryAttribute
        self["electronicCheck"] = electronicCheck
    
    
class QasiAddress(dict):
    def __init__(self, value:str, unrestricted_value) -> None:
        """
        :param "value": "c. Moscow, street. Kekovaya h.13",
        :param "unrestricted_value": null
        
        return None
        """
        
        self["value"] = value
        self["unrestricted_value"] = unrestricted_value 
        
    def append_data(self,
                    city:str=None,
                    house:str=None,
                    region:str=None,
                    street:str=None,
                    country:str=None) -> None:
        """
        :param "city": "Moscow",
        :param "house": "13",
        :param "region": "",
        :param "street": "street. Kekovaya",
        :param "country": "Russia"
        """
        
        if "data" not in self:
            self["data"] = []
        data = {
            "city": city,
            "house": house,
            "region": region,
            "street": street,
            "country": country
            },
        data = AqsiFunctions.body_filter(data)
        if data == {}:
            raise Exception("You should create minimum 1 argument")
        self["data"].append(data)
