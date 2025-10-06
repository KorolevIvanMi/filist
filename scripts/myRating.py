from kivy.uix.accordion import StringProperty
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import StringProperty

class CustomButtonForRationg(Button):
    pass

class CustomLayotForRating(BoxLayout):
    selected_rating = StringProperty("")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.width = 100
        self.orientation = 'horizontal'
        for i in range(5):
            btn = CustomButtonForRationg(text = str(i+1))
            btn.bind(on_release = lambda btn: self.buttonIsDown(btn.text))
            self.add_widget(btn)
    def buttonIsDown(self, txt):
        print("Выбран рейтинг"+ txt)
        self.selected_rating = txt
        