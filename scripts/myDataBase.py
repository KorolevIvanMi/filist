import sqlite3 as sq

class myDataBase:
    def __init__(self, dp_path = "B:/Filist project/dataBase/film_base.db"):
        self.db_path = dp_path
    def db_init(self):
        with sq.connect(self.db_path) as con:
            cur = con.cursor()

            cur.execute('''
            CREATE TABLE IF NOT EXISTS filmlist(
            film_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            status INTEGER NOT NULL,
            rating INTEGER NOT NULL,
            discription TEXT NOT NULL )
            ''')
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


if __name__ == "__main__":
    db = myDataBase()
    db.db_init()
