import importlib
from typing import NoReturn

import View.MainScreen.main_screen
from kivymd.app import MDApp
from Controller.detail_screen import DetailScreenController
importlib.reload(View.MainScreen.main_screen)

APP = MDApp.get_running_app()
class MainScreenController:
    def __init__(self, model):
        self.model = model
        self.view = View.MainScreen.main_screen.MainScreenView(controller=self, model=self.model)

    def refresh_callback(self) -> NoReturn:
        self.model.check_data()
        
    def get_view(self) -> View.MainScreen.main_screen.MainScreenView:
        return self.view
