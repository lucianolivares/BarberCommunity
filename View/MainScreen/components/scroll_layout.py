import os
from typing import NoReturn, Union

from kivy.animation import Animation
from kivy.core.window import Window
from kivy.effects.dampedscroll import DampedScrollEffect
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ColorProperty, NumericProperty, ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView

from kivymd import uix_path
from kivymd.theming import ThemableBehavior

Builder.load_string('''
#:import Window kivy.core.window.Window


<RefreshSpinner>

    AnchorLayout:
        id: body_spinner
        size_hint: None, None
        size: dp(46), dp(46)
        y: Window.height
        pos_hint: {'center_x': .5}
        anchor_x: 'center'
        anchor_y: 'center'

        canvas:
            Clear
            Color:
                rgba: (1, 0, 0, 0)
            Ellipse:
                pos: self.pos
                size: self.size

        MDSpinner:
            id: spinner
            size_hint: None, None
            size: dp(30), dp(30)
            color: app.theme_cls.primary_color
            line_width: dp(3)
''')


class _RefreshScrollEffect(DampedScrollEffect):
    """
    This class is simply based on DampedScrollEffect.
    If you need any documentation please look at
    :class:`~kivy.effects.dampedscrolleffect`.
    """

    min_scroll_to_reload = NumericProperty("-100dp")
    """
    Minimum overscroll value to reload.

    :attr:`min_scroll_to_reload` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `'-100dp'`.
    """

    def on_overscroll(
        self, instance_refresh_scroll_effect, overscroll: Union[int, float]
    ) -> bool:
        if overscroll < self.min_scroll_to_reload:
            scroll_view = self.target_widget.parent
            scroll_view._did_overscroll = True
            return True
        else:
            return False


class ScrollLayout(ScrollView):
    root_layout = ObjectProperty()
    """
    The spinner will be attached to this layout.

    :attr:`root_layout` is a :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.effect_cls = _RefreshScrollEffect
        self._work_spinnrer = False
        self._did_overscroll = False
        self.refresh_spinner = None

    def on_touch_up(self, *args):
        if self._did_overscroll and not self._work_spinnrer:
            if self.refresh_callback:
                self.refresh_callback()
            if not self.refresh_spinner:
                self.refresh_spinner = RefreshSpinner(_refresh_layout=self)
                self.root_layout.add_widget(self.refresh_spinner)
            self.refresh_spinner.start_anim_spinner()
            self._work_spinnrer = True
            self._did_overscroll = False
            return True

        return super().on_touch_up(*args)

    def refresh_done(self) -> NoReturn:
        if self.refresh_spinner:
            self.refresh_spinner.hide_anim_spinner()


class RefreshSpinner(ThemableBehavior, FloatLayout):
    spinner_color = ColorProperty([1, 1, 1, 1])
    """
    Color of spinner.

    :attr:`spinner_color` is a :class:`~kivy.properties.ColorProperty`
    and defaults to `[1, 1, 1, 1]`.
    """

    # kivymd.refreshlayout.MDScrollViewRefreshLayout object
    _refresh_layout = ObjectProperty()

    def start_anim_spinner(self) -> NoReturn:
        spinner = self.ids.body_spinner
        Animation(
            y=spinner.y - self.theme_cls.standard_increment * 2 + dp(10),
            d=0.8,
            t="out_elastic",
        ).start(spinner)

    def hide_anim_spinner(self) -> NoReturn:
        spinner = self.ids.body_spinner
        anim = Animation(y=Window.height, d=0.8, t="out_elastic")
        anim.bind(on_complete=self.set_spinner)
        anim.start(spinner)

    def set_spinner(self, *args) -> NoReturn:
        body_spinner = self.ids.body_spinner
        body_spinner.size = (dp(46), dp(46))
        body_spinner.y = Window.height
        body_spinner.opacity = 1
        spinner = self.ids.spinner
        spinner.size = (dp(30), dp(30))
        spinner.opacity = 1
        self._refresh_layout._work_spinnrer = False
        self._refresh_layout._did_overscroll = False
