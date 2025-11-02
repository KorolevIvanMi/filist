from kivy.uix.accordion import NumericProperty
from kivy.uix.accordion import BooleanProperty
from kivy.config import Config
Config.set('graphics', 'width', '1920')
Config.set('graphics', 'height', '1080')
Config.set('graphics', 'resizable', False) 
from kivy.app import App
from kivy.lang import Builder
import os
from kivy.properties import (
     BooleanProperty, NumericProperty
)
from kivy.uix.screenmanager import ScreenManager, Screen
from FillistMainMenu import FillistMainMenu
from addFilmMenu import AddFilmMenu
from redactFilmMenu import RedactFilmMenu

class mainScreen(Screen):
    pass

class AddFilmMenuScreen(Screen):
    pass

class RedactFilmMenuScreen(Screen):
    pass

class FillistApp(App):
        data_updated = BooleanProperty(False)
        film_updated = BooleanProperty(False)
        film_to_redact = NumericProperty(-1)
        def build(self):
            # СНАЧАЛА загружаем KV файл
            kv_path = os.path.join(os.path.dirname(__file__), '..', 'design', 'fillist.kv')
            Builder.load_file(kv_path)
            
            # ПОТОМ создаем виджеты
            sm = ScreenManager()
            sm.add_widget(mainScreen())
            sm.add_widget(AddFilmMenuScreen())
            sm.add_widget(RedactFilmMenuScreen())
            return sm
        

if __name__ == '__main__':
    FillistApp().run()