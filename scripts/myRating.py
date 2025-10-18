from kivy.uix.accordion import StringProperty
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import StringProperty

class CustomButtonForRationg(Button):
    pass

class CustomLayotForRating(BoxLayout):
    selected_rating = StringProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.width = 100
        buttons = []
        self.orientation = 'horizontal'
        for i in range(5):
            btn = CustomButtonForRationg(text = str(i+1))
            btn.bind(on_release = lambda btn: self.buttonIsDown(btn.text, buttons))
            buttons.append(btn)
            self.add_widget(btn)

    def buttonIsDown(self, txt, buttons):    
        self.selected_rating = txt
        for button in buttons:
            button.background_color = (136/255,136/255,136/255, 1)
        for button in buttons:
            if int(button.text) <= int(txt):
                button.background_color = (1,204/255,0, 1)
    

    