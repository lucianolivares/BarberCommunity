from typing import NoReturn

from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from Utility.observer import Observer


class ProfileScreenView(MDScreen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()


    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)
        self.ids.topbar.ids.title.text = 'Perfil'
        self.ids.navbar.ids.profile_button.icon = 'account-circle'

    def model_is_changed(self) -> NoReturn:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
