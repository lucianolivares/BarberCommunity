from Model.main_screen import MainScreenModel
from Model.login_screen import LoginScreenModel
from Model.profile_screen import ProfileScreenModel

from Controller.main_screen import MainScreenController
from Controller.login_screen import LoginScreenController
from Controller.profile_screen import ProfileScreenController


screens = {
    "main screen": {
        "model": MainScreenModel,
        "controller": MainScreenController,
    },
    "profile screen": {
        "model": ProfileScreenModel,
        "controller": ProfileScreenController,
    },
    "login screen": {
        "model": LoginScreenModel,
        "controller": LoginScreenController,
    },
}
