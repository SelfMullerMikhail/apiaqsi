import sys
import os

from .aqsi_requests import ApiAqsiClasses
from .aqsi_body.cashiers import CashiersAqsi
from .aqsi_body.clients import ClientsAqsi
from .aqsi_body.devices import DeviceAqsi
from .aqsi_body.goods import GoodsAqsi
from .aqsi_body.goodsCategory import GoodsCategoryAqsi
from .aqsi_body.orders import OrdersAqsi
from .aqsi_body.receipts import ReceiptsAqsi
from .aqsi_body.shifts import ShiftsAqsi
from .aqsi_body.shops import ShopsAqsi
from .aqsi_body.slips import Slips