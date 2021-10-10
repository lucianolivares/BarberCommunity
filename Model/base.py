import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from typing import Union
import requests


class Base:
    def __init__(self):
        try:
            self.cloud = firebase_admin.initialize_app(name='cloud')
        except:
            self.cloud = firebase_admin.get_app('cloud')

        self.client = firestore.client(self.cloud)

    def get_barbers_data(self) -> Union[dict, None]:
        """
        Return colletion from the database:
        """

        try:
            data = self.client.collection('barbershops').get()
        except requests.exceptions.ConnectionError:
            return None
        return data



'''
    def send_user_data_to_database(self, data: dict) -> bool:
        """Sends data to the database."""

        try:
            self.real_time_firebase.put(
                f"{self.type_base}/{self.name_base_users}",
                get_time(),
                data,
            )
            return True
        except requests.exceptions.HTTPError:
            return False
'''
