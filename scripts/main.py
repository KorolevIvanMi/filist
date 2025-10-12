from kivy.config import Config
Config.set('graphics', 'width', '1920')
Config.set('graphics', 'height', '1080')
Config.set('graphics', 'resizable', False) 
from kivy.app import App
from kivy.lang import Builder
import os
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from FillistMainMenu import FillistMainMenu


class FillistApp(App):
    def build(self):
        
        kv_path = os.path.join(os.path.dirname(__file__), '..', 'design', 'fillist.kv')
        Builder.load_file(kv_path)
        application = FillistMainMenu()
        return application

if __name__ == '__main__':
    FillistApp().run()