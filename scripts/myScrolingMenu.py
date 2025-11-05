from kivy.uix.actionbar import partial
from kivy.uix.accordion import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import BooleanProperty, StringProperty, NumericProperty
from myDataBase import myDataBase
from kivy.app import App

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
        self.rating = data.get('rating', 0)
        self.film_id = data.get('film_id', '')
        super(StatefulLabel, self).refresh_view_attrs(rv, index, data)
        self.update_rating_buttons()

    def del_btn_realise(self, btn):
        db = myDataBase()
        db.del_film(self.film_id)
        if hasattr(self.parent.parent, 'update_data'):
            new_data = db.get_all_films()
            self.parent.parent.update_data(new_data)

    def update_rating_buttons(self):
        # Ждем пока все виджеты создадутся
        from kivy.clock import Clock
        Clock.schedule_once(self._update_rating_buttons)

    def _update_rating_buttons(self, dt):
        """Фактическое обновление кнопок"""
        if not hasattr(self, 'ids'):
            return
            
        # Ищем кнопки рейтинга (они находятся во втором BoxLayout)
        rating_layout = None
        for child in self.children:
            if isinstance(child, BoxLayout) and len(child.children) == 5:
                # Это layout с кнопками рейтинга
                rating_layout = child
                break
        
        if rating_layout:
            for i, button in enumerate(rating_layout.children[::-1]):  # reversed
                rating_value = i + 1
                if rating_value <= self.rating:
                    # Кнопка активная - другой цвет
                    button.background_normal = ('./images/buttons/rating_btn_down.png') # Золотой для активных
                else:
                    # Кнопка неактивная - серый цвет
                    button.background_normal = ('./images/buttons/rating_btn_up.png')
    def go_to_update_film(self):
        app = App.get_running_app()
        app.film_to_redact = self.film_id
        
        app.root.current = "redactFilmMenuScreen"

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

        