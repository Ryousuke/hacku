import sqlite3

conn=sqlite3.connect('review_db.db')
cursor=conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS review_comments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        professor_number TEXT,
        comment TEXT
    )
''')

conn.commit()

conn.close()