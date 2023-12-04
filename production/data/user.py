import sqlite3

conn=sqlite3.connect('user_db.db')
cursor=conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        university TEXT,
        faculity TEXT
    )
''')

conn.commit()

conn.close()