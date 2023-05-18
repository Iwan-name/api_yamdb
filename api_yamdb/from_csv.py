import sqlite3
import pandas

df = pandas.read_csv('D:/Dev/api_yamdb/api_yamdb/static/data/users.csv')

df.columns = df.columns.str.strip()
connection = sqlite3.connect('db.sqlite3')

df.to_sql('users_user', connection, if_exists='append')
