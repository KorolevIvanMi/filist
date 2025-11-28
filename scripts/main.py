from kivy.uix.accordion import NumericProperty
from kivy.uix.accordion import BooleanProperty
from kivy.config import Config
Config.set('graphics', 'width', '1920')
Config.set('graphics', 'height', '1080')
Config.set('graphics', 'resizable', True) 
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
from utils import load_kv_file

class mainScreen(Screen):
    pass

class AddFilmMenuScreen(Screen):
    pass

class RedactFilmMenuScreen(Screen):
    def on_enter(self, *args):
        # Этот метод вызывается автоматически при входе на экран
        if self.ids.redact_film_menu:  # Проверяем, что виджет существует
            self.ids.redact_film_menu.setup_all_data()

class FillistApp(App):
        data_updated = BooleanProperty(False)
        
        film_to_redact = NumericProperty(-1)
        def build(self):
            # СНАЧАЛА загружаем KV файл
            load_kv_file('design/fillist.kv')  # ← ИСПРАВЛЕНО
    
    # ПОТОМ создаем виджеты
            sm = ScreenManager()
            sm.add_widget(mainScreen())
            sm.add_widget(AddFilmMenuScreen())
            sm.add_widget(RedactFilmMenuScreen())
            return sm

if __name__ == '__main__':
    FillistApp().run()