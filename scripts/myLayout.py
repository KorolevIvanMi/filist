
from kivy.lang import Builder
import os
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from myDropDown import StatusDropdown

class myLayout(FloatLayout):
    search_but = ObjectProperty(None)
    search_text = ObjectProperty(None)
    status_dropdown = None
    status_button = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setup_status_dropdown()

    def setup_status_dropdown(self):
        #Настройка dropdown для статуса
        self.status_dropdown = StatusDropdown()
        self.status_dropdown.bind(on_select=self.on_status_select)

    def searchOnPress(self):
        text_to_find = self.search_text.text
        self.search_text.text = "Поиск..."
        print("Пользователь ищет: "+ text_to_find)
    
    def open_status_dropdown(self):
        #Открывает dropdown статуса
        if self.status_dropdown and self.status_button:
            self.status_dropdown.open(self.status_button)

    def on_status_select(self, instance, value):
        # Обновляем текст кнопки на выбранный статус
        if self.status_button:
            self.status_button.text = value