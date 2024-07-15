import sqlite3

url_db = './data/shop.sqlite3'

create_table_sql = """CREATE TABLE IF NOT EXISTS users(
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT NOT NULL,
                      user TEXT NOT NULL,
                      pswd TEXT NOT NULL
                      )"""

insert_user_sql = f"INSERT INTO users(name, user, pswd)VALUES(?,?,?)"


def connect_db():
  conn = sqlite3.connect(url_db)
  cur = conn.cursor()
  return conn , cur


def create_table_user():
  conn, cur = connect_db()
  cur.execute(create_table_sql)
  conn.commit()
  conn.close()

def insert_user(user_data):
  conn, cur = connect_db()
  cur.execute(insert_user_sql,user_data)
  conn.commit()
  conn.close()