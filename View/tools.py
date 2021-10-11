from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout

Builder.load_string('''
<NavBar>:
    canvas:
        Color:
            rgba: (0, 0, 0, 0.5)
        Line:
            width: dp(0.25)
            points: self.x, self.height, self.width, self.height
    size_hint_y: None
    height: dp(50)

    MDIconButton:
        id: barbers_button
        pos_hint: {'center_x': 0.2}
        icon: 'face-man-shimmer-outline'
        on_release: app.manager_screens.current = 'main screen'
    MDIconButton:
        pos_hint: {'center_x': 0.35}
        icon: 'store-outline' 
    MDIconButton:
        pos_hint: {'center_x': 0.5}
        icon: 'checkbox-multiple-marked-outline'
    MDIconButton:
        pos_hint: {'center_x': 0.65}
        icon: 'map-marker-radius-outline'
    MDIconButton:
        id: profile_button
        pos_hint: {'center_x': 0.8}
        icon: 'account-circle-outline'
        on_release: app.manager_screens.current = 'profile screen'

<TopBar>:
    canvas:
        Color:
            rgba: (0, 0, 0, 0.5)
        Line:
            width: dp(0.25)
            points: self.x, self.y, self.width, self.y

    adaptive_height: True
    height: dp(50)
    padding: (dp(10), 0, dp(10), 0)
    spacing: (dp(10),)
    cols: 2
    MDLabel:
        id: title
        font_style: 'H4'
        font_name: 'assets/fonts/vintage_party/VintageParty-FreeVersion.ttf'
''')

class NavBar(MDFloatLayout):
    pass

class TopBar(MDGridLayout):
    pass