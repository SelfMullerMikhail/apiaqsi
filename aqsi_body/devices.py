import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_dir)

import requests


class DeviceAqsi:
    def __init__(self, API):
        self.__HEADERS = API

    def device_index(self) -> dict:
        """
        Obtaining all devices within the external system

        return: A dictionary containing the list of devices.
        """
        url_api = "https://api.aqsi.ru/pub/v1/Devices"
        return requests.get(url_api, headers=self.__HEADERS)
