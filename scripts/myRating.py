from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class CustomButtonForRationg(Button):
    pass
class CustomLayotForRating(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.width = 100
        self.orientation = 'horizontal'
        for i in range(5):
            btn = CustomButtonForRationg(text = str(i+1))
            self.add_widget(btn)