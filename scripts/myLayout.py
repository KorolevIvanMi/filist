from kivy.uix.settings import text_type

from kivy.lang import Builder
import os
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.clock import Clock
from myDropDown import StatusDropdown
from myRating import CustomLayotForRating
from myDataBase import myDataBase
from myScrolingMenu import RV, StatefulLabel, RecycleGridLayout
class myLayout(FloatLayout):
    
    db = myDataBase()
    rating_layout = ObjectProperty(None)
    search_but = ObjectProperty(None)
    search_text = ObjectProperty(None)
    status_dropdown = None
    status_button = ObjectProperty(None)
    rating_layout = None
    scroll_menu = ObjectProperty(None) 
    accept_filrs_btn = ObjectProperty(None)
    reset_filtrs_btn = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.rating_layout = CustomLayotForRating()
        self.setup_status_dropdown()
        
        
        Clock.schedule_once(self.setup_scroling_menu, 0.1)
        
# Поиск по названию
    def searchOnPress(self):
        text_to_find = self.search_text.text
        self.search_text.text = "Поиск..."
        s = self.db.find_film_by_name(text_to_find)
        if(text_to_find == "Поиск..." or text_to_find == "all"):
             data_from_db = self.db.get_all_films()
             self.scroll_menu.update_data(data_from_db)
        else:
            self.scroll_menu.update_data(s)

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


# Обработка выбора рейтинга
    def on_rating_selected(self, value):
       
        print(f"Выбран рейтинг: {value}")
        
    def setup_scroling_menu(self, dt = None):
        data_from_db = self.db.get_all_films()
        print(data_from_db)
        if self.scroll_menu:
            self.scroll_menu.update_data(data_from_db)

            
    def refresh_scroll_menu(self):

        self.setup_scroling_menu()

        