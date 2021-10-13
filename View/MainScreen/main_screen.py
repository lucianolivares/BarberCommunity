from typing import Union, NoReturn

from kivy.properties import ObjectProperty
from kivy.clock import Clock

from kivymd.uix.screen import MDScreen
from Utility.observer import Observer
from View.MainScreen.components import barber_card


class MainScreenView(MDScreen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)
        self.controller.refresh_callback()
        self.ids.refresh_layout.start_spinner()
        self.ids.topbar.ids.title.text = 'Barberias'
        self.ids.navbar.ids.barbers_button.icon = 'face-man-shimmer'

    def load_barbers(self, interval: Union[int, float]):
        self.ids.barbers_grid.clear_widgets()
        barbers = self.controller.get_barbers()
        for barber, data in barbers.items():
            card = barber_card.BarberCard(data=data, id=barber, controller=self.controller)
            self.ids.barbers_grid.add_widget(card)
            self.ids.refresh_layout.refresh_done()

    def load_barber(self):
        #self.ids.barbers_grid.clear_widgets()
        barber = self.model.barber
        card = barber_card.BarberCard(data=barber, id=barber, controller=self.controller)
        self.ids.barbers_grid.add_widget(card)
        
    def model_is_changed(self) -> NoReturn:
        if self.model.get_data_status:
            Clock.schedule_once(self.load_barbers, 1)

        if self.model.get_data_status is False:
            pass