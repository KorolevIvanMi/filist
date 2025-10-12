import sqlite3 as sq

class myDataBase:
    def __init__(self, db_path="B:/Filist project/dataBase/film_base.db"):
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

if __name__ == "__main__":
    db = myDataBase()
    db.db_init()