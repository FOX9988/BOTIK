import sqlite3

Connection = sqlite3.connect('data.db')
sql = Connection.cursor()




sql.execute('create table if not exists users (id integer primary key autoincrement, name text, number text, telegram_id integer);')


def register_user(name, number, telegram_id):
    Connection = sqlite3.connect('data.db')
    sql = Connection.cursor()



    sql.execute('insert into users (name, number, telegram_id) values (?,?,?);')
    Connection.commit