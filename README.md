# apiaqsi
                                    APIAqsi
                              
  APIAqsi is a Python library that simplifies interaction with the Aqsi cash
register system by providing an easy-to-use API. This library is developed
by SelfMullerMikhail as a part of an educational project and is aimed at
making it easier for developers to work with Aqsi cash registers.

Full documentation 'https://api.aqsi.ru/#section/Opisanie'
-------------------------------------------------------------------------------
                             Installation (yet no......)
                            
To install APIAqsi, simply use pip:

pip install apiaqsi

-------------------------------------------------------------------------------
                                Usage (yet no......)
                              
Here's an example of how to use APIAqsi to retrieve the current status of a cash register:

from apiaqsi import AqsiAPI
API = "gIZ4jaquN7aTET6gOYOsVnFdnqYmoyrPWEdlRbaTlUIi0N3zwB1VO0ek56y198vL"
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

-------------------------------------------------------------------------------

Contributors
SelfMullerMikhail (https://github.com/SelfMullerMikhail)
