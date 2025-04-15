import psycopg2
# import csv

current_user = ''

conn = psycopg2.connect( # creating a connection
    database="snake_db",
    user="postgres",
    host="localhost",
    password="12345",
    port=5432,
)


query_create_table_users = """
    CREATE TABLE users(
        id SERIAL PRIMARY KEY,
        username VARCHAR(255) UNIQUE
    )
"""

query_create_table_user_scores = """
    CREATE TABLE user_scores(
        id SERIAL PRIMARY KEY,
        username VARCHAR(255),
        score INTEGER,
        level INTEGER
    )
"""

def execute_query(query):
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def input_user():
    global current_user
    current_user = input()

def add_user(name):
    command = "INSERT INTO users(username) VALUES(%s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (name,))
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def check_if_user_exists(name):
    command = "SELECT username FROM users WHERE username = %s"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (name,))
            result = cur.fetchall()
            return bool(result)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def add_new_score(score, lvl):
    command = "INSERT INTO user_scores(username, score, level) VALUES(%s, %s, %s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (current_user, score, lvl))
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def process_score(score, lvl):
    user_exists = check_if_user_exists(current_user)
    # print(user_exists)
    if not user_exists: 
        add_user(current_user)
    add_new_score(score, lvl)

def show_highest_level():
    command = "SELECT MAX(level) FROM user_scores WHERE username = %s"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (current_user,))
            result = cur.fetchall()
            return result
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    

if __name__ == '__main__':
    input_user()
    process_score(10, 1)
    # execute_query(query_create_table_users)
    # execute_query(query_create_table_user_scores)