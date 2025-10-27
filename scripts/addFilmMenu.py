from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.app import App
class AddFilmMenu(Widget):
    add_film_btn = ObjectProperty(None)

    def acceptOnRelease(self):
        app = App.get_running_app()
        app.root.current = "mainScreen"