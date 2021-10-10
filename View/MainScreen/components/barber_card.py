from kivymd.uix.card import MDCard
from kivy.lang import Builder
from kivymd.uix.label.label import MDLabel


Builder.load_string('''
<BarberCard>:

    md_bg_color: 1, 1, 1, 0.9
    elevation: 10
    radius: (36,)


    FitImage:
        radius: (36, 0, 0,36)
        size_hint_x: 0.4
        source: 'assets/images/default.jpeg'

    BoxLayout:
        id: labels
        orientation: 'vertical'
        MDLabel:
            id: name
            text: 'Nombre: '
            md_bg_color: 1, 0, 0, 0.2
        MDLabel:
            id: address
            text: 'Ubicacion: '
        MDLabel:
            id: city
            text: 'Ciudad: '
        MDLabel:
            text: 'Dueno:'
        MDLabel:
            text: 'Celular:'
'''
)

class BarberCard(MDCard):
    def __init__(self, **kw):
        super().__init__()
        self.kind_dialog = kw['data']
        for key, value in self.kind_dialog.items():
            self.ids.city.text = 'asdfasdghfdsf'

