from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
import kivy
import os

class FillistMainMenu(Widget):
    pass
class FillistApp(App):
    def build(self):
        kv_path = os.path.join(os.path.dirname(__file__), '..', 'design', 'fillist.kv')
        Builder.load_file(kv_path)
        return FillistMainMenu()

if __name__ == '__main__':
    FillistApp().run()