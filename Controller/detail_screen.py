import importlib
from typing import NoReturn

import View.DetailScreen.detail_screen

importlib.reload(View.DetailScreen.detail_screen)

class DetailScreenController:
    def __init__(self, model):
        self.model = model
        self.view = View.DetailScreen.detail_screen.DetailScreenView(controller=self, model=self.model)
    
    def load_data(self, id):
        self.model.get_barber(id)

    def get_view(self) -> View.DetailScreen.detail_screen.DetailScreenView:
        return self.view
