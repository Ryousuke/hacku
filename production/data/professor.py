import sqlite3

conn=sqlite3.connect('professor_db.db')
cursor=conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS professors(
        id INTEGER PRYMARY KEY AUTOINCREMENT,
        name TEXT,
        hometown TEXT,
        hobby1 TEXT,
        hobby2 TEXT,
        campus TEXT,
        faculity TEXT,
        baseball_team TEXT,
        specializedField TEXT,
        animal TEXT,
        music TEXT
    )
''')

conn.commit()

conn.close()