# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.

from Model.main_screen import MainScreenModel
from Model.login_screen import LoginScreenModel

from Controller.main_screen import MainScreenController
from Controller.login_screen import LoginScreenController
from View.MainScreen.components.barber_card import BarberCard
screens = {
    "login screen": {
        "model": LoginScreenModel,
        "controller": LoginScreenController,
    },
    "main screen": {
        "model": MainScreenModel,
        "controller": MainScreenController,
    },
}
