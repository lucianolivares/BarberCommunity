import importlib
from typing import NoReturn

import View.MainScreen.main_screen
from kivy.clock import Clock

importlib.reload(View.MainScreen.main_screen)


class MainScreenController:
    def __init__(self, model):
        self.model = model
        self.view = View.MainScreen.main_screen.MainScreenView(controller=self, model=self.model)

    def refresh_callback(self) -> NoReturn:
        self.model.check_data()

    def get_barbers(self):
        return self.model.barbers

    def get_barber(self, id):
        self.model.get_barber(id)

    def get_view(self) -> View.MainScreen.main_screen.MainScreenView:
        return self.view
