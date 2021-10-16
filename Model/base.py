from firebase import Firebase
from typing import Union
import requests


class Base:
    def __init__(self):
        config = {
            "apiKey": "AIzaSyATIca3Yy3zEkepeVJ376p9F-Mypfx35E0",
            "authDomain": "barbercommunity-chile.firebaseapp.com",
            "databaseURL": "https://barbercommunity-chile-default-rtdb.firebaseio.com/",
            "storageBucket": "gs://barbercommunity-chile.appspot.com/",
            "serviceAccount": "barbercommunity-chile-firebase-adminsdk-jxse3-33a15ab491.json"
        }

        firebase = Firebase(config)

        self.db = firebase.database()

    def get_barbers_data(self) -> Union[list, None]:
        """
        Return colletion from the database:
        """

        try:
            data = self.db.child('barbershops').get()
        except requests.exceptions.ConnectionError:
            return None
        return data
    
    def get_barber(self, id) -> Union[dict, None]:
        """
        Return colletion from the database:
        """

        try:
            data = self.db.child('barbershops').child(id).get()
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
