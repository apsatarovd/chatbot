import psycopg2 

DATABASE = 'postgres'
USER = 'postgres'
PASSWORD = 'password'
HOST = 'localhost'
PORT = '5434'

conn = psycopg2.connect(
    dbname=DATABASE,
    user=USER,
    password=PASSWORD,
    host=HOST,
    port=PORT
)

cursor = conn.cursor()

conn.close()


