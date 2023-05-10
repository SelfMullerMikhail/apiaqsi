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
from headers_function import get_header


class ApiAqsiClasses:
    def __init__(self, STRIPE_SECRET_KEY:str) -> dict:
        """ 
        Full documentation 'https://api.aqsi.ru/#section/Opisanie'
        
        This class returns classes for working with individual URL addresses.
        
        :param API: <str>
        """
        self.__STRIPE_SECRET_KEY = STRIPE_SECRET_KEY
        return None
        
    def __str__(self):
        return """
        Full documentation 'https://api.aqsi.ru/#section/Opisanie'
        GitHub: 'https://github.com/SelfMullerMikhail/apiaqsi'
        Create by Mikhail Korniushenko
        """
        
    def get_shops(self) -> ShopsAqsi:
        return ShopsAqsi(self.__STRIPE_SECRET_KEY)
    
    def get_devices(self) -> DeviceAqsi:
        return DeviceAqsi(self.__STRIPE_SECRET_KEY)
    
    def get_cashiers(self) -> CashiersAqsi:
        return CashiersAqsi
    
    def get_receipts(self) -> ReceiptsAqsi:
        return ReceiptsAqsi(self.__STRIPE_SECRET_KEY)
        
    def get_slips(self) -> Slips:
        return Slips(self.__STRIPE_SECRET_KEY) 
    
    def get_shifts(self) -> ShiftsAqsi:
        return ShiftsAqsi(self.__STRIPE_SECRET_KEY)
    
    def get_goodsCategory(self) -> GoodsCategoryAqsi:
        return GoodsCategoryAqsi(self.__STRIPE_SECRET_KEY)
    
    def get_goods(self) -> GoodsAqsi:
        return GoodsAqsi(self.__STRIPE_SECRET_KEY)
    
    def get_clietns(self) -> ClientsAqsi:
        return ClientsAqsi(self.__STRIPE_SECRET_KEY)
    
    def get_orders(self) -> OrdersAqsi:
        return OrdersAqsi(self.__STRIPE_SECRET_KEY)
        
