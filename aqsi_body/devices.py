import sys
import os
import requests

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_dir)
from headers_function import get_header



class DeviceAqsi:
    def __init__(self, STRIPE_SECRET_KEY:str) -> None:
        self.__HEADERS = get_header(STRIPE_SECRET_KEY)

    def device_index(self) -> dict:
        """
        Obtaining all devices within the external system

        return: A dictionary containing the list of devices.
        """
        url_api = "https://api.aqsi.ru/pub/v1/Devices"
        return requests.get(url_api, headers=self.__HEADERS)
