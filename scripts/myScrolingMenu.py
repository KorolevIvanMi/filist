from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import BooleanProperty, StringProperty

class StatefulLabel(RecycleDataViewBehavior, BoxLayout):
    name = StringProperty()
    genre = StringProperty()
    status = StringProperty()
    active = BooleanProperty()
    index = 0

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        self.name = data.get('name', '')
        self.genre = data.get('genre', '')
        self.status = data.get('status', '')
        super(StatefulLabel, self).refresh_view_attrs(rv, index, data)

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
                {'name': 'Фильм 1', 'genre': 'Драма', 'status': 'Новый', 'active': False},
                {'name': 'Фильм 2', 'genre': 'Комедия', 'status': 'Просмотрено', 'active': False},
                {'name': 'Фильм 3', 'genre': 'Боевик', 'status': 'В процессе', 'active': False},
                {'name': 'Фильм 4', 'genre': 'Фантастика', 'status': 'Новый', 'active': False},
                {'name': 'Фильм 5', 'genre': 'Ужасы', 'status': 'Просмотрено', 'active': False},
            ]
        self.data = data_list