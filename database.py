import sqlite3
from task_1 import data_for_db

# connect to a db
conn = sqlite3.connect('books.db')

# create a cursor
cur = conn.cursor()

# create a table 
cur.execute("""CREATE TABLE IF NOT EXISTS books(
        id varchar,
        title text,
        author text,
        genre text,
        publisher text,
        year int,
        price real,
        currency text
        )""")
cur.executemany("INSERT INTO books VALUES (?,?,?,?,?,?,?,?)", data_for_db)
cur.execute("""CREATE TABLE IF NOT EXISTS summary_transformation AS 
        SELECT year,
        count(*) AS count_book,
        ROUND(AVG(CASE
                WHEN currency = '€' THEN price * 1.2
                ELSE price END),2) AS average_currency
        FROM books
        GROUP BY year
       
        """)

# commit our command 
conn.commit()

# close our connection
conn.close()