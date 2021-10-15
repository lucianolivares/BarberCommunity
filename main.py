import importlib
import os
from typing import NoReturn

from kivy import Config
from kivy.uix.screenmanager import NoTransition, ScreenManager

from PIL import ImageGrab
from Model.base import Base

# TODO: You may know an easier way to get the size of a computer display.
resolution = ImageGrab.grab().size

# Change the values of the application window size as you need.
Config.set("graphics", "height", '800')
Config.set("graphics", "width", "480")
#Config.set("graphics", "height", resolution[1])
#Config.set("graphics", "width", "400")

# Place the application window on the right side of the computer screen.
from kivy.core.window import Window
Window.top = 0
Window.left = resolution[0] - Window.width


from kivymd.tools.hotreload.app import MDApp


class BarberCommunity(MDApp):
    KV_FILES = {
        os.path.join(
            os.getcwd(),
            "View",
            "MainScreen",
            "main_screen.kv",
        ),
        os.path.join(
            os.getcwd(),
            "View",
            "DetailScreen",
            "detail_screen.kv",
        ),
        os.path.join(
            os.getcwd(),
            "View",
            "LoginScreen",
            "login_screen.kv",
        ),
        os.path.join(
            os.getcwd(),
            "View",
            "ProfileScreen",
            "profile_screen.kv",
        ),
    }

    def build_app(self) -> ScreenManager:
        """
        In this method, you don't need to change anything other than the
        application theme.
        """

        import View.screens

        self.theme_cls.primary_palette = "Red"
        self.manager_screens = ScreenManager(transition=NoTransition())
        self.base = Base()
        Window.bind(on_key_down=self.on_keyboard_down)
        importlib.reload(View.screens)
        screens = View.screens.screens

        for i, name_screen in enumerate(screens.keys()):
            model = screens[name_screen]["model"](self.base)
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)
            
        self.manager_screens.current = 'main screen'
        return self.manager_screens

    def on_keyboard_down(self, window, keyboard, keycode, text, modifiers) -> NoReturn:
        """
        The method handles keyboard events.

        By default, a forced restart of an application is tied to the
        `CTRL+R` key on Windows OS and `COMMAND+R` on Mac OS.
        """

        if "meta" in modifiers or "ctrl" in modifiers and text == "r":
            self.rebuild()


BarberCommunity().run()


'''
from typing import NoReturn

from kivy.uix.screenmanager import ScreenManager

from kivymd.app import MDApp

from View.screens import screens


class BarberCommunity(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)
        # This is the screen manager that will contain all the screens of your
        # application.
        self.manager_screens = ScreenManager()
      
    def build(self) -> ScreenManager:
        """
        Initializes the application; it will be called only once.
        If this method returns a widget (tree), it will be used as the root
        widget and added to the window.

        :return:
            None or a root :class:`~kivy.uix.widget.Widget` instance
            if no self.root exists.
        """

        self.theme_cls.primary_palette = "Amber"
        self.generate_application_screens()
        return self.manager_screens

    def generate_application_screens(self) -> NoReturn:
        """
        Creating and adding screens to the screen manager.
        You should not change this cycle unnecessarily. He is self-sufficient.

        If you need to add any screen, open the `View.screens.py` module and
        see how new screens are added according to the given application
        architecture.
        """
        self.base = Base()

        for i, name_screen in enumerate(screens.keys()):
            model = screens[name_screen]["model"](self.base)
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)

BarberCommunity().run()
'''