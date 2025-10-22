from kivy.uix.widget import Widget
from myLayout import myLayout
from kivy.app import App


class FillistMainMenu(Widget):
    # переход на экран добавления фильма
    def go_to_addScreen(self):
        app = App.get_running_app()
        app.root.current = "AddFilmMenuScreen"