import psycopg2

conn = psycopg2.connect(
    dbname="testdb",
    user="dias",
    password="12345",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50),
        email VARCHAR(100),
        age INTEGER
    )
""")

conn.commit()
cur.close()
conn.close()