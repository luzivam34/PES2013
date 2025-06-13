import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="250717",
        host="localhost"
    )
    return conn

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:250717@localhost:5432/postgres'
SQLALCHEMY_TRACK_MODIFICATIONS = False
