from kivy.uix.actionbar import partial
from kivy.uix.accordion import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import BooleanProperty, StringProperty, NumericProperty
from myDataBase import myDataBase

class StatefulLabel(RecycleDataViewBehavior, BoxLayout):
    name = StringProperty()
    genre = StringProperty()
    status = StringProperty()
    rating = NumericProperty()
    active = BooleanProperty()
    index = 0

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        self.name = data.get('name', '')
        self.genre = data.get('genre', '')
        self.status = data.get('status', '')
        self.rating = data.get('rating', '')
        self.film_id = data.get('film_id', '')
        super(StatefulLabel, self).refresh_view_attrs(rv, index, data)

    def del_btn_realise(self, btn):
        db = myDataBase()
        db.del_film(self.film_id)
        if hasattr(self.parent.parent, 'update_data'):
            new_data = db.get_all_films()
            self.parent.parent.update_data(new_data)

class RecycleGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(RecycleGridLayout, self).__init__(**kwargs)
        self.bind(minimum_height=self.setter('height'))   

class RV(RecycleView):
    def __init__(self, data_list=None, **kwargs):
        super(RV, self).__init__(**kwargs)
        
        
        if data_list is None:
            # Данные по умолчанию, если список не передан
            data_list = [
                {'name': 'Фильм 1', 'genre': 'Драма', 'status': 'Новый', 'rating': 4, 'film_id': 1,'active': False}
            ]
        self.data = data_list
    def update_data(self, new_data_list):
        self.data = new_data_list
    
        