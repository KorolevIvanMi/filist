from kivy.uix.accordion import BooleanProperty
from kivy.config import Config
Config.set('graphics', 'width', '1920')
Config.set('graphics', 'height', '1080')
Config.set('graphics', 'resizable', False) 
from kivy.app import App
from kivy.lang import Builder
import os
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, BooleanProperty
)
from kivy.uix.screenmanager import ScreenManager, Screen
from FillistMainMenu import FillistMainMenu
from addFilmMenu import AddFilmMenu

class mainScreen(Screen):
    pass

class AddFilmMenuScreen(Screen):
    pass

class FillistApp(App):
        data_updated = BooleanProperty(False)

        def build(self):
            # СНАЧАЛА загружаем KV файл
            kv_path = os.path.join(os.path.dirname(__file__), '..', 'design', 'fillist.kv')
            Builder.load_file(kv_path)
            
            # ПОТОМ создаем виджеты
            sm = ScreenManager()
            sm.add_widget(mainScreen())
            sm.add_widget(AddFilmMenuScreen())
            return sm
        
        def mark_data_updated(self):
            """Отметить, что данные нужно обновить"""
            self.data_updated = True

        def clear_data_updated(self):
            """Сбросить флаг обновления"""
            self.data_updated = False
if __name__ == '__main__':
    FillistApp().run()