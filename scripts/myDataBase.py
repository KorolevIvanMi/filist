import sqlite3 as sq


class myDataBase:
    def __init__(self, db_path="./dataBase/film_base.db"):
        self.db_path = db_path
    def db_init(self):
        pre_films = [
            ("Зелёная миля", 1, 2, 4, "Фильм жестокий, но очень поучительный и ценный"),
            ("Я-легенда", 2, 1, 0, ""),
            ("Наруто", 3, 3, 0, "")
        ]
        statuses = [
            ("В планах",),
            ("Просмотрен",),
            ("В процессе",)
        ]
        pre_genres = [
            ("тёмное фэнтези",),
            ("ужасы",),
            ("фэнтези",)
        ]
        ratings = [
            (1,),
            (2,),
            (3,),
            (4,),
            (5,)
        ]
        
        with sq.connect(self.db_path) as con:
            cur = con.cursor()

        
            cur.execute('''
            CREATE TABLE IF NOT EXISTS status(
            status_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL)
            ''')
            
            cur.execute('''
            CREATE TABLE IF NOT EXISTS rating(
            rating_id INTEGER PRIMARY KEY AUTOINCREMENT,
            value INTEGER NOT NULL)
            ''')
            
            cur.execute('''
            CREATE TABLE IF NOT EXISTS genre(
            genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL)
            ''')
            
           
            cur.execute('''
            CREATE TABLE IF NOT EXISTS filmlist(
            film_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            genre INTEGER NOT NULL,
            status INTEGER NOT NULL,
            rating INTEGER NOT NULL,
            description TEXT NOT NULL)
            ''')
            
            
            for status in statuses:
                cur.execute('INSERT INTO status (name) VALUES(?)', status)
            
            for rating in ratings:
                cur.execute('INSERT INTO rating (value) VALUES(?)', rating)
            
            for genre in pre_genres:
                cur.execute('INSERT INTO genre (name) VALUES(?)', genre)
            
           
            for film in pre_films:
                cur.execute('''INSERT INTO filmlist (name, genre, status, rating, description) 
                            VALUES(?, ?, ?, ?, ?)''', film)
    
    def find_film_by_name(self, film_name):
        with sq.connect(self.db_path) as con:
            con.row_factory = sq.Row 
            cur = con.cursor()
            cur.execute('''
                        SELECT filmlist.name,   genre.name as genre_name,  status.name as status_name, rating, filmlist.description, filmlist.film_id FROM filmlist
                        JOIN genre ON filmlist.genre  = genre.genre_id
                        JOIN status ON filmlist.status = status.status_id
                        WHERE filmlist.name = ?
                        ''', (film_name,))
            results = cur.fetchall()
            
            films = []
            for row in results:
                film_dict = {
                    'name': row['name'],
                    'genre': row['genre_name'],  
                    'status': row['status_name'], 
                    'rating': row['rating'],
                    
                    'description': row['description'], 
                    'film_id': row['film_id'],
                    'active': False,  
                }
                films.append(film_dict)
            
            return films
        
    def get_all_films(self):
        with sq.connect(self.db_path) as con:
            con.row_factory = sq.Row 
            cur = con.cursor()
            cur.execute('''
                        SELECT filmlist.name,   genre.name as genre_name,  status.name as status_name, rating, filmlist.description, filmlist.film_id FROM filmlist
                        JOIN genre ON filmlist.genre  = genre.genre_id
                        JOIN status ON filmlist.status = status.status_id
                        ''')
            results = cur.fetchall()
            films = []
            for row in results:
                film_dict = {
                    'name': row['name'],
                    'genre': row['genre_name'],  
                    'status': row['status_name'], 
                    'rating': row['rating'],
                    'active': False,  
                    'description': row['description'] , 
                    'film_id': row['film_id']
                }
                films.append(film_dict)
            return films
    def del_film(self, film_id):
            
        with sq.connect(self.db_path) as con:
            cur = con.cursor()
            cur.execute('''DELETE FROM filmlist where film_id = ?''', (film_id,))
            
            return 0

    def find_films_with_filters(self, film_status, film_rating):
         with sq.connect(self.db_path) as con:
            con.row_factory = sq.Row 
            cur = con.cursor()
            if(film_rating != '' and film_status != "Все"):
                cur.execute('''
                            SELECT filmlist.name,   genre.name as genre_name,  status.name as status_name, rating, filmlist.description, filmlist.film_id FROM filmlist
                            JOIN genre ON filmlist.genre  = genre.genre_id
                            JOIN status ON filmlist.status = status.status_id
                            WHERE status.name = ? AND rating = ?
                            ''', (film_status, film_rating))
            elif(film_rating != '' and film_status == "Все"):
                cur.execute('''
                            SELECT filmlist.name,   genre.name as genre_name,  status.name as status_name, rating, filmlist.description, filmlist.film_id FROM filmlist
                            JOIN genre ON filmlist.genre  = genre.genre_id
                            JOIN status ON filmlist.status = status.status_id
                            WHERE rating = ?
                            ''', (film_rating,))    
            elif(film_rating == '' and film_status == "Все"):
                cur.execute('''
                            SELECT filmlist.name,   genre.name as genre_name,  status.name as status_name, rating, filmlist.description, filmlist.film_id FROM filmlist
                            JOIN genre ON filmlist.genre  = genre.genre_id
                            JOIN status ON filmlist.status = status.status_id
                            ''')
            elif(film_rating == '' and film_status != "Все"):
                cur.execute('''
                            SELECT filmlist.name,   genre.name as genre_name,  status.name as status_name, rating, filmlist.description, filmlist.film_id FROM filmlist
                            JOIN genre ON filmlist.genre  = genre.genre_id
                            JOIN status ON filmlist.status = status.status_id
                            WHERE status.name = ? 
                            ''', (film_status,))
            results = cur.fetchall()
            films = []
            for row in results:
                film_dict = {
                    'name': row['name'],
                    'genre': row['genre_name'],  
                    'status': row['status_name'], 
                    'rating': row['rating'],
                    
                    'description': row['description'], 
                    'film_id': row['film_id'],
                    'active': False,  
                }
                films.append(film_dict)
            return films
         
    def add_film_to_bd(self, film_name, film_genre, film_status, film_rating, film_discription):
        with sq.connect(self.db_path) as con:
            con.row_factory = sq.Row 
            cur = con.cursor()
            # проверка существования фильма
            cur.execute('''
                        SELECT filmlist.name,   genre.name as genre_name,  status.name as status_name, rating, filmlist.description, filmlist.film_id FROM filmlist
                        JOIN genre ON filmlist.genre  = genre.genre_id
                        JOIN status ON filmlist.status = status.status_id
                        WHERE filmlist.name = ? AND genre.name = ?
						AND status.name = ? AND rating = ?
                        ''', (film_name, film_genre, film_status, film_rating,))
            results = cur.fetchall()
            films = []
            for row in results:
                film_dict = {
                    'name': row['name'],
                    'genre_id': row['genre_id']
                }
                films.append(film_dict)
            if(films == []):
                # добавление жанра в таблицу жанров и формирование genre_id
                genre_id = -1
                cur.execute('''SELECT * from genre where name = ?''', (film_genre,))
                results = cur.fetchall()
                films = []
                for row in results:
                    film_dict = {
                        'name': row['name'],
                        'genre_id': row['genre_id']
                    }
                    films.append(film_dict)
                if (films == []):
                    cur.execute('''INSERT INTO genre(name) VALUES (?)''', (film_genre,))
                    genre_id = cur.lastrowid
                else:
                    genre_id = films[0]['genre_id']
                # добавление статуса фильма и формирования status_id
                status_id = -1
                cur.execute('''SELECT * from genre where name = ?''', (film_status,))
                results = cur.fetchall()
                films = []
                for row in results:
                    film_dict = {
                        'name': row['name'],
                        'status_id': row['status_id']
                    }
                    films.append(film_dict)
                status_id = films[0][status_id]
                # создание rating_id
                rating_id = film_rating
                results = cur.fetchall()
                films = []
                for row in results:
                    film_dict = {
                        'name': row['name'],
                        'genre_id': row['genre_id']
                    }
                    films.append(film_dict)
                # добавление фильма в таблицу
                cur.execute('''INSERT INTO filmlist(name, genre, status, rating, description) VALUES (?, ?, ?, ?, ?)''', 
                            (film_name, genre_id, status_id, rating_id, film_discription, ))
                print("Фильм добавлет в таблицу")
                return 1
            else:
                print("Такой фильм уже существует, попробуйте заного")
                return 0     
            

        
        
if __name__ == "__main__":
    db = myDataBase()
    db.db_init()
    