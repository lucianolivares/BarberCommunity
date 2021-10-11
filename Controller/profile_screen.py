import importlib
from typing import NoReturn

import View.ProfileScreen.profile_screen

importlib.reload(View.ProfileScreen.profile_screen)


class ProfileScreenController:
    def __init__(self, model):
        self.model = model
        self.view = View.ProfileScreen.profile_screen.ProfileScreenView(controller=self, model=self.model)

    def get_view(self) -> View.ProfileScreen.profile_screen.ProfileScreenView:
        return self.view
