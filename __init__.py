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

from aqsi_types.aqsi_types import *