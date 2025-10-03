from kivy.uix.settings import text_type
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
import os
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
class myLayout(FloatLayout):
    search_but = ObjectProperty(None)
    search_text = ObjectProperty(None)
    def searchOnPress(self):
        text_to_find = self.search_text.text
        self.search_text.text = "Поиск..."
        print("Пользователь ищет: "+ text_to_find)