from typing import Union, NoReturn

from kivy.properties import ObjectProperty
from kivy.clock import Clock

from kivymd.uix.screen import MDScreen
from Utility.observer import Observer
from View.MainScreen.components import barber_card
from View.MainScreen.components import scroll_layout

class MainScreenView(MDScreen, Observer):
    """
    A class that implements a visual representation of the model data
    :class:`~Model.main_screen.MainScreenModel`.

    Implements the login start screen in the user application.
    """

    controller = ObjectProperty()
    """
    Controller object - :class:`~Controller.main_screen.MainScreenController`.

    :attr:`controller` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    model = ObjectProperty()
    """
    Model object - :class:`~Model.main_screen.MainScreenModel`.

    :attr:`model` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    manager_screens = ObjectProperty()
    """
    Screen manager object - :class:`~kivy.uix.screenmanager.ScreenManager`.

    :attr:`manager_screens` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)
    def on_pre_enter(self, *args):
        self.controller.refresh_callback()

    def load_barbers(self, interval: Union[int, float]):
        self.ids.barbers_grid.clear_widgets()
        barbers = self.controller.get_barbers()
        for barber, data in barbers.items():
            # Imagen, Nombre, Ubicacion, Administrador, celular,
            widget = barber_card.BarberCard(data=data)
            self.ids.barbers_grid.add_widget(widget)
            self.ids.refresh_layout.refresh_done()

    def model_is_changed(self) -> NoReturn:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        if self.model.get_data_status:
            Clock.schedule_once(self.load_barbers, 1)

        if self.model.get_data_status is False:
            pass
