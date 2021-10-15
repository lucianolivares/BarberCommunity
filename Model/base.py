import firebase_admin
from firebase_admin import firestore, credentials, auth
from typing import Union
import requests


class Base:
    def __init__(self):
        try:
            cred = credentials.Certificate("barbercommunity-chile-firebase-adminsdk-jxse3-33a15ab491.json")
            self.cloud = firebase_admin.initialize_app(cred, name='cloud')
        except:
            self.cloud = firebase_admin.get_app('cloud')

        self.client = firestore.client(self.cloud)

    def get_barbers_data(self) -> Union[list, None]:
        """
        Return colletion from the database:
        """

        try:
            data = self.client.collection('barbershops').get()
        except requests.exceptions.ConnectionError:
            return None
        return data
    
    def get_barber(self, id) -> Union[dict, None]:
        """
        Return colletion from the database:
        """

        try:
            data = self.client.collection('barbershops')
            data = data.document(id).get().to_dict()
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
