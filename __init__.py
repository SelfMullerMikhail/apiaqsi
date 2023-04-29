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

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_dir)

from functions.aqsi_functions import AqsiFunctions
from aqsi_types.aqsi_types import *

API = ""
aqsi = ApiAqsiClasses(API)

shops = aqsi.get_shops()
orders = aqsi.get_orders()
goods = aqsi.get_goods()
device = aqsi.get_devices()
cachiers = aqsi.get_cashiers()
reciepts = aqsi.get_receipts()
slips = aqsi.get_slips()
shifts = aqsi.get_shifts()
goods_category = aqsi.get_goodsCategory()
clients = aqsi.get_clietns()

content_order = ContentOrder(type_= 4, discountMoney=5.5)
orders.orders_create(id=2, number="4", content=content_order)