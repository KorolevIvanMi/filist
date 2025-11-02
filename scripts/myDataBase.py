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
    # Очистка и нормализация данных
        film_name = film_name.strip()
        film_genre = film_genre.strip().lower()  # Приводим к нижнему регистру
        film_status = film_status.strip()
        film_rating = str(film_rating).strip() if film_rating else "0"
        film_discription = film_discription.strip()
        
        # Отладочная печать
        print(f"Поиск фильма: '{film_name}', '{film_genre}', '{film_status}', '{film_rating}'")
        
        with sq.connect(self.db_path) as con:
            con.row_factory = sq.Row 
            cur = con.cursor()
            
            # Проверка существования фильма (исправленный запрос)
            cur.execute('''
                SELECT filmlist.name, filmlist.genre as genre_id, 
                    genre.name as genre_name, status.name as status_name, 
                    rating, filmlist.description, filmlist.film_id 
                FROM filmlist
                JOIN genre ON filmlist.genre = genre.genre_id
                JOIN status ON filmlist.status = status.status_id
                WHERE LOWER(filmlist.name) = LOWER(?) 
                AND LOWER(genre.name) = LOWER(?)
                AND LOWER(status.name) = LOWER(?)
                AND rating = ?
            ''', (film_name, film_genre, film_status, film_rating))
            
            results = cur.fetchall()
            print(f"Найдено совпадений: {len(results)}")
            
            if not results:  # Фильм не найден
                # Добавление жанра в таблицу жанров и формирование genre_id
                genre_id = -1
                cur.execute('''SELECT * from genre where LOWER(name) = LOWER(?)''', (film_genre,))
                results = cur.fetchall()
                films = []
                for row in results:
                    film_dict = {
                        'name': row['name'],
                        'genre_id': row['genre_id']
                    }
                    films.append(film_dict)
                
                if not films:
                    # Добавляем жанр в нижнем регистре
                    cur.execute('''INSERT INTO genre(name) VALUES (?)''', (film_genre,))
                    genre_id = cur.lastrowid
                    print(f"Добавлен новый жанр: {film_genre} (id: {genre_id})")
                else:
                    genre_id = films[0]['genre_id']
                    print(f"Найден существующий жанр: {film_genre} (id: {genre_id})")
                
                # Добавление статуса фильма и формирование status_id
                status_id = -1
                cur.execute('''SELECT * from status where LOWER(name) = LOWER(?)''', (film_status,))
                results = cur.fetchall()
                films = []
                for row in results:
                    film_dict = {
                        'name': row['name'],
                        'status_id': row['status_id']
                    }
                    films.append(film_dict)
                
                if films:
                    status_id = films[0]['status_id']
                    print(f"Найден статус: {film_status} (id: {status_id})")
                else:
                    # Если статус не найден, можно добавить его или использовать значение по умолчанию
                    print(f"Статус '{film_status}' не найден в базе!")
                    return 0
                
                # Подготовка рейтинга
                rating_id = film_rating
                if rating_id == "":
                    rating_id = "0"
                
                # Добавление фильма в таблицу
                cur.execute('''INSERT INTO filmlist(name, genre, status, rating, description) VALUES (?, ?, ?, ?, ?)''', 
                            (film_name, genre_id, status_id, rating_id, film_discription))
                
                con.commit()
                print("Фильм успешно добавлен в таблицу")
                return 1
            else:
                print("Такой фильм уже существует, попробуйте заного")
                # Вывод информации о найденных дубликатах для отладки
                for row in results:
                    print(f"Найден дубликат: {row['name']} (id: {row['film_id']}), жанр: {row['genre_name']}, статус: {row['status_name']}, рейтинг: {row['rating']}")
                return 0

    def find_film_by_id(self, film_id):
        with sq.connect(self.db_path) as con:
            con.row_factory = sq.Row 
            cur = con.cursor()
            film_id_int = int(film_id)
            cur.execute('''
                        SELECT filmlist.name, genre.name as genre_name, status.name as status_name, 
                            rating, filmlist.description, filmlist.film_id 
                        FROM filmlist
                        JOIN genre ON filmlist.genre = genre.genre_id
                        JOIN status ON filmlist.status = status.status_id
                        WHERE filmlist.film_id = ?
                        ''', (film_id_int,))
            result = cur.fetchone()  # Используем fetchone()
            
            if result:
                film_dict = {
                    'name': result['name'],
                    'genre': result['genre_name'],  
                    'status': result['status_name'], 
                    'rating': result['rating'],
                    'description': result['description'], 
                    'film_id': result['film_id'],
                    'active': False,  
                }
                return film_dict
            return None
                
    