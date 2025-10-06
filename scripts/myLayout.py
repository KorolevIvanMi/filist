from kivy.uix.settings import text_type

from kivy.lang import Builder
import os
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from myDropDown import StatusDropdown
from myRating import CustomLayotForRating
class myLayout(FloatLayout):
    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        search_but = ObjectProperty(None)
        search_text = ObjectProperty(None)
        status_dropdown = None
        # rating_text = ObjectProperty(None)
        status_button = ObjectProperty(None)
        rating_layout = None
        self.rating_layout = CustomLayotForRating()
        self.setup_status_dropdown()
        
# Поиск по названию
    def searchOnPress(self):
        text_to_find = self.search_text.text
        self.search_text.text = "Поиск..."
        print("Пользователь ищет: "+ text_to_find)

# обработка dropdown меню
    def setup_status_dropdown(self):
        #Настройка dropdown для статуса
        self.status_dropdown = StatusDropdown()
        self.status_dropdown.bind(on_select=self.on_status_select)

    def open_status_dropdown(self):
        #Открывает dropdown статуса
        if self.status_dropdown and self.status_button:
            self.status_dropdown.open(self.status_button)

    def on_status_select(self, instance, value):
        # Обновляем текст кнопки на выбранный статус
        if self.status_button:
            self.status_button.text = value
# настройка рейтинга небольшая
    def on_rating_selected(self):
        selected_rating = self.rating_layout.selected_rating
        print("Выбран рейтинг"+ str(selected_rating))
        
 

        