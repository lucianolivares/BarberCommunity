import importlib
from typing import NoReturn

import View.LoginScreen.login_screen

importlib.reload(View.LoginScreen.login_screen)


class LoginScreenController:
    def __init__(self, model):
        self.model = model
        self.view = View.LoginScreen.login_screen.LoginScreenView(controller=self, model=self.model)

    def on_tap_button_login(self) -> NoReturn:
        """Called when the `LOGIN` button is pressed."""

    def set_user_data(self, key, value) -> NoReturn:
        """Called every time the user enters text into the text fields."""

    def get_view(self) -> View.LoginScreen.login_screen.LoginScreenView:
        return self.view
