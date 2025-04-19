import psycopg2
import csv

conn = psycopg2.connect( # creating a connection
    database="phonebook",
    user="postgres",
    host="localhost",
    password="12345",
    port=5432,
)


def execute_query(query):
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


# FILTER BY 1'st LETTER FUNCTION
create_func_filter_by_first_letter = """
    CREATE OR REPLACE FUNCTION filter_by_first_letter(letter VARCHAR(1))
    RETURNS TABLE (id INTEGER, user_name VARCHAR(255), phone VARCHAR(12))
    AS
    $$
    BEGIN
        RETURN QUERY
        SELECT * FROM phonebook WHERE LEFT(phonebook.user_name, 1) = letter;
    END;
    $$
    LANGUAGE plpgsql;
"""
def call_function_w_args(function_name, args):
    try:
        with conn.cursor() as cur:
            cur.callproc(function_name, args)
            return cur.fetchall()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
# execute_query(create_func_filter_by_first_letter)
# letter = tuple((input("Enter the first letter: ")).upper())
# print(call_function_w_args('filter_by_first_letter', letter))




# INSERT PROCEDURE 
create_procedure_insert_new =   """
    CREATE OR REPLACE PROCEDURE add_new_user(
    new_user_name VARCHAR,
    new_phone VARCHAR(12)
    )
    AS $$
    BEGIN
        -- If user already exists, update the phone number
        IF EXISTS (SELECT 1 FROM phonebook WHERE user_name = new_user_name) THEN
            UPDATE phonebook
            SET phone = new_phone
            WHERE user_name = new_user_name;
        ELSE
            -- Otherwise, insert a new user
            INSERT INTO phonebook(user_name, phone)
            VALUES(new_user_name, new_phone);
        END IF;
    END;
    $$
    LANGUAGE plpgsql;
"""     
def insert_new(user, phone):
    user_to_insert = (user, phone)
    command = "CALL add_new_user(%s, %s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, user_to_insert)
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
# user = input("Enter user name: ")
# phone = input("Enter phone number: ")
# insert_new(user, phone)




# INSERT PROCEDURE FOR MULTIPLE USERS
create_procedure_insert_new_list=   """ 
    CREATE OR REPLACE PROCEDURE add_new_user(
        new_user_name varchar,
        new_phone varchar(12)
    ) 
    AS $$
    BEGIN
        -- insert into the phonebook table
        INSERT INTO phonebook(user_name, phone)
        VALUES(new_user_name, new_phone);
    END;
    $$
    LANGUAGE PLPGSQL;
"""     
def insert_new_list(users_to_insert): 

    command = "CALL add_new_user(%s, %s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, users_to_insert) 
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
# users_to_insert = [ 
#     ('Raim', '+77077070000'), 
#     ('Alexandra', '+77077878787'), 
#     ('Jennifer', '+77077878787') 
# ]
# for user in users_to_insert:
#     insert_new_list(user)




# DELETE PROCEDURE
create_procedure_delete_user = """
    CREATE OR REPLACE PROCEDURE delete_user(user_2_del VARCHAR, phone_2_del VARCHAR(12))
    AS $$
    BEGIN
        DELETE FROM phonebook WHERE phonebook.user_name = user_2_del OR phonebook.phone = phone_2_del;
    END;
    $$
    LANGUAGE plpgsql;
"""
def delete_user(user, phone):
    user_to_delete = (user, phone)
    command = "CALL delete_user(%s, %s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, user_to_delete)
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# user_2_del = input("Enter user name(Enter if you delete by phone): ")
# if user_2_del == '':
#     phone_2_del = input("Enter phone number: ")
#     delete_user(user_2_del, phone_2_del)
# else:
#     phone_2_del = ''
#     delete_user(user_2_del, phone_2_del)


MENU = """
1. Insert new user
2. Insert new user from csv file
3. Delete user
4. Filter by first letter
5. Exit
"""
while True:
    print(MENU)
    choice = input("Enter your choice: ")
    if choice == '1':     # insert user
        user_name = input("Enter user name: ")
        phone = input("Enter phone number: ")
        insert_new(user_name, phone)
    elif choice == '2':   # insert from csv
        csv_file_name = input("Enter csv file name without (.csv): ")
        with open(f"{csv_file_name}.csv", 'r') as file:
            reader = csv.reader(file)
            _ = next(reader) # getting rid of the headers
            for row in reader:
                insert_new_list(row)
    elif choice == '3':   # delete user
        user_2_del = input("Enter user name (Enter if you want to delete by phone): ")
        if user_2_del == '':
            phone_2_del = input("Enter phone number: ")
            delete_user(user_2_del, phone_2_del)
        else:
            phone_2_del = ''
            delete_user(user_2_del, phone_2_del)
    elif choice == '4':   # filter by first letter
        letter = tuple((input("Enter the first letter: ")).upper())
        print(call_function_w_args('filter_by_first_letter', letter))
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")