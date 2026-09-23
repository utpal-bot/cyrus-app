from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse, Line
from kivy.clock import Clock

class ArcReactor(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_reactor, 1/60)

    def update_reactor(self, dt):
        self.canvas.clear()
        with self.canvas:
            Color(0, 0.9, 1, 0.9)
            center_x = self.width / 2
            center_y = self.height / 2
            Line(circle=(center_x, center_y, 110), width=2)
            Line(circle=(center_x, center_y, 80), width=4)
            Color(1, 1, 1, 1)
            Ellipse(pos=(center_x - 30, center_y - 30), size=(60, 60))

class CyrusApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        status = Label(text="CYRUS ONLINE - BOSS", font_size='22sp', color=(0, 0.9, 1, 1))
        reactor = ArcReactor()
        layout.add_widget(status)
        layout.add_widget(reactor)
        return layout

if __name__ == '__main__':
    CyrusApp().run()
