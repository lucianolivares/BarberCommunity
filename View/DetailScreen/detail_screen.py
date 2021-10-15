from typing import Union, NoReturn

from kivy.properties import ObjectProperty, StringProperty
from kivy.clock import Clock

from kivymd.uix.screen import MDScreen
from Utility.observer import Observer



class DetailScreenView(MDScreen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()
    barber = StringProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)
        self.ids.navbar.ids.barbers_button.icon = 'face-man-shimmer'
    
    def on_pre_enter(self):
        self.controller.load_data(self.barber)
    
    def on_leave(self):
        self.ids.topbar.ids.title.text = ''

    def load_barber(self):
        self.ids.topbar.ids.title.text = self.model.barber['name']

    def model_is_changed(self) -> NoReturn:
        if self.model.get_data_status:
            self.load_barber()

        if self.model.get_data_status is False:
            pass