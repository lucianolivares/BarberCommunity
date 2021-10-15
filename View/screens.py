from Model.main_screen import MainScreenModel
from Model.login_screen import LoginScreenModel
from Model.profile_screen import ProfileScreenModel
from Model.detail_screen import DetailScreenModel

from Controller.main_screen import MainScreenController
from Controller.login_screen import LoginScreenController
from Controller.profile_screen import ProfileScreenController
from Controller.detail_screen import DetailScreenController


screens = {
    "main screen": {
        "model": MainScreenModel,
        "controller": MainScreenController,
    },
    "detail screen": {
        "model": DetailScreenModel,
        "controller": DetailScreenController,
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
