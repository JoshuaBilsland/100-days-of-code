# This class is responsible for talking to the Google Sheet.
import os
import requests


class DataManager:
    def __init__(self):
        self.__sheet_endpoint = os.environ.get("SHEET_ENDPOINT")

    def sheety_get(self):
        return requests.get(url=self.__sheet_endpoint)

    def sheety_put(self, row_id, new_data):
        response = requests.put(
            url=f"{self.__sheet_endpoint}/{row_id}", json=new_data)
        response.raise_for_status()
