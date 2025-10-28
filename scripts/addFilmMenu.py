from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.app import App
from myDropDown import StatusDropdown
from kivy.clock import Clock
class AddFilmMenu(Widget):
    add_film_btn = ObjectProperty(None)

    status_button = ObjectProperty(None)
    status_dropdown = None
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.setup_status_dropdown()

        
    def acceptOnRelease(self):
        app = App.get_running_app()
        app.root.current = "mainScreen"
    def setup_status_dropdown(self):
        #Настройка dropdown для статуса
        self.status_dropdown = StatusDropdown()
        self.status_dropdown.bind(on_select=self.on_status_select)

    def open_status_dropdown(self):
        print("Open dropDown")
        #Открывает dropdown статуса
        if self.status_dropdown and self.status_button:
            self.status_dropdown.open(self.status_button)
    def on_status_select(self, instance, value):

        # Обновляем текст кнопки на выбранный статус
        if self.status_button:
            self.status_button.text = value
