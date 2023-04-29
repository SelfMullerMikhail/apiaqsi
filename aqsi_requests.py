from .aqsi_body.cashiers import CashiersAqsi
from .aqsi_body.clients import ClientsAqsi
from .aqsi_body.devices import DeviceAqsi
from .aqsi_body.goods import GoodsAqsi
from .aqsi_body.goodsCategory import GoodsCategoryAqsi
from .aqsi_body.orders import OrdersAqsi
from .aqsi_body.receipts import ReceiptsAqsi
from .aqsi_body.shops import ShopsAqsi
from .aqsi_body.slips import Slips
from .aqsi_body.shifts import ShiftsAqsi


class ApiAqsiClasses:
    def __init__(self, API:str) -> dict:
        """ 
        Full documentation 'https://api.aqsi.ru/#section/Opisanie'
        
        This class returns classes for working with individual URL addresses.
        
        :param API: <str>
        """
        self.__API = API
        self.__HEADERS = {"x-client-key": f"Application {self.__API}"}
        return self.__HEADERS
        
    def __str__(self):
        return """
        Full documentation 'https://api.aqsi.ru/#section/Opisanie'
        Create by Mikhail Korniushenko
        """
        
    def get_shops(self) -> ShopsAqsi:
        return ShopsAqsi(self.__HEADERS)
    
    def get_devices(self) -> DeviceAqsi:
        return DeviceAqsi(self.__HEADERS)
    
    def get_cashiers(self) -> CashiersAqsi:
        return CashiersAqsi
    
    def get_receipts(self) -> ReceiptsAqsi:
        return ReceiptsAqsi(self.__HEADERS)
        
    def get_slips(self) -> Slips:
        return Slips(self.__HEADERS) 
    
    def get_shifts(self) -> ShiftsAqsi:
        return ShiftsAqsi(self.__HEADERS)
    
    def get_goodsCategory(self) -> GoodsCategoryAqsi:
        return GoodsCategoryAqsi(self.__HEADERS)
    
    def get_goods(self) -> GoodsAqsi:
        return GoodsAqsi(self.__HEADERS)
    
    def get_clietns(self) -> ClientsAqsi:
        return ClientsAqsi(self.__HEADERS)
    
    def get_orders(self) -> OrdersAqsi:
        return OrdersAqsi(self.__HEADERS)
        