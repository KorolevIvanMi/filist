
from kivy.lang import Builder
import os
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.uix.button import Button


class myLayout(FloatLayout):
    search_but = ObjectProperty(None)
    search_text = ObjectProperty(None)
    


    def searchOnPress(self):
        text_to_find = self.search_text.text
        self.search_text.text = "Поиск..."
        print("Пользователь ищет: "+ text_to_find)
