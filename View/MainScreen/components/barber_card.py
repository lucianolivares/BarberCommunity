from kivy.uix.behaviors.button import ButtonBehavior
from kivymd.uix.card import MDCard
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from View.DetailScreen.detail_screen import DetailScreenView

Builder.load_string('''
<BarberCard>:
    md_bg_color: 1, 1, 1, 0.9
    elevation: 10
    radius: (20,)

    FitImage:
        id: image
        radius: (20, 0, 0,20)
        size_hint_x: 0.4
        # Cargar imagenes de storage proto
        source: 'assets/images/'

    BoxLayout:
        id: labels
        orientation: 'vertical'
        padding: 8
        MDLabel:
            id: name
            markup: True
            shorten:True
            text: 'Nombre: [b]'
            #md_bg_color: 1, 0, 0, 0.2
        MDLabel:
            id: address
            markup: True
            shorten:True
            text: 'Ubicacion: [b]'
        MDLabel:
            id: city
            markup: True
            shorten:True
            text: 'Ciudad: [b]'
        MDLabel:
            id: owner
            markup: True
            shorten:True
            text: 'Dueño: [b]'
        MDLabel:
            id: mobile
            markup: True
            shorten:True
            text: 'Celular: [b]'
'''
)

class BarberCard(MDCard, ButtonBehavior):

    def __init__(self, **kw):
        super().__init__()
        self.controller = kw['controller']
        self.barber = kw['data']
        self.id = kw['id']
        self.on_release = self.barber_detail

        for key, value in self.barber.items():
            if key == 'mobile':
                self.ids[f'{key}'].text += str(value[4:])
            elif key == 'image':
                self.ids[f'{key}'].source += str(value)
            else:
                self.ids[f'{key}'].text += str(value)

    def barber_detail(self):
        from kivymd.app import MDApp
        app = MDApp.get_running_app()
        screen = app.manager_screens.get_screen('detail screen')
        screen.barber = self.id
        app.manager_screens.current = 'detail screen'