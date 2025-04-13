import psycopg2
import csv

conn = psycopg2.connect( # creating a connection
    database="phonebook",
    user="postgres",
    host="localhost",
    password="5647Radmir",
    port=5432,
)

# Creating table if it doesn't exist
def create_table():

# Check if the table already exists
    command = "SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'phonebook')"
    with conn.cursor() as cur:
        cur.execute(command)
        exists = cur.fetchone()[0]

    if exists:
        print("Table already exists.")
        return
    
    command = """CREATE TABLE phonebook (
                id SERIAL PRIMARY KEY,
                user_name VARCHAR(255),
                phone VARCHAR(12)
            )"""
    

    with conn.cursor() as cur:
        # execute the command
        cur.execute(command)
        conn.commit()
        
    ch = input("Table created successfully. Press Enter to continue...")
    return ch

# Delete table if it exists
def drop_table():
    command = "DROP TABLE IF EXISTS phonebook"

    with conn.cursor() as cur:
        # execute the command
        cur.execute(command)
        conn.commit()



# Insert user by terminal
def insert(user_name, phone):

    command = "INSERT INTO phonebook(user_name, phone) VALUES(%s, %s)"

    with conn.cursor() as cur:
        # execute the command
        cur.execute(command, (user_name, phone))
        conn.commit()

# Insert from csv file
def insert_from_csv(csv_file_name):

    command = "INSERT INTO phonebook(user_name, phone) VALUES(%s, %s)"

    with conn.cursor() as cur:
        # execute the command
        with open(csv_file_name, "r") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            _ = next(csvreader) # getting rid of the headers
            for row in csvreader:
                user_name, phone = row
                cur.execute(command, (user_name, phone))
        conn.commit()



# Get names filter by first letter
def get_names_filter_by_letter(letter):
    command = "SELECT * FROM phonebook WHERE user_name LIKE %s"
    with conn.cursor() as cur:
        cur.execute(command, (letter,)) # (,) is to show that we have a tuple
        results = cur.fetchall()
        if not results:
            print("No users found starting with that letter.")
        else:
            for row in results:
                print(row)

# Get names filter by provider
def get_names_filter_by_provider(provider):
    provider_prefixes = {
        'kcell': ['701', '702', '775', '778'],
        'beeline': ['705', '777'],
        'tele2': ['707', '747'],
        'altel': ['708', '709', '770', '700'],
    }

    prefixes = provider_prefixes.get(provider.lower())
    if not prefixes:
        print("Unknown provider.")
        return

    with conn.cursor() as cur:
        results = []
        for prefix in prefixes:
            # проверяем и номера с +7 и с 8
            cur.execute("""
                SELECT * FROM phonebook 
                WHERE phone LIKE %s OR phone LIKE %s
            """, (f'+7{prefix}%', f'8{prefix}%'))
            results += cur.fetchall()
        
        if not results:
            print("No entries found for this provider.")
        else:
            for row in results:
                print(row)


        
# Update name
def update_user_name():
    # current_name = input("Enter current user name: ")
    current_phone = input("Enter current phone number: ")
    new_name = input("Enter new user name: ")

    command = "UPDATE phonebook SET user_name = %s WHERE phone = %s"
    with conn.cursor() as cur:
        cur.execute(command, (new_name, current_phone))
        if cur.rowcount == 0:
            print("No matching user found.")
        else:
            print("User name updated successfully.")
        conn.commit()

# Update phone number
def update_user_phone():
    # current_name = input("Enter current user name: ")
    current_phone = input("Enter current phone number: ")
    new_phone = input("Enter new phone number: ")

    command = "UPDATE phonebook SET phone = %s WHERE phone = %s"
    with conn.cursor() as cur:
        cur.execute(command, (new_phone, current_phone))
        if cur.rowcount == 0:
            print("No matching user found.")
        else:
            print("Phone number updated successfully.")
        conn.commit()



# DELETE USER
def delete_user(phone):
   
    command = "DELETE FROM phonebook WHERE phone = %s"

    with conn.cursor() as cur:
        cur.execute(command, (phone,))
        conn.commit()

#Select all users
def select_all():
    command = "SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'phonebook')"
    with conn.cursor() as cur:
        cur.execute(command)
        exists = cur.fetchone()[0]
    if exists:
        command = "SELECT * FROM phonebook"
    else:
        print("Table does not exist.")
        # return empty list if table does not exist
        return

    with conn.cursor() as cur:
        cur.execute(command)
        return cur.fetchall()

data = select_all()

# Main menu
MENU = """
1. Create table 
2. Drop table
3. Insert user
4. Insert from csv
5. Get users filter by 
6. Update user information
7. Delete user
8. Show database
9. Exit
"""
while True:

    print(MENU)
    choice = input("Enter your choice: ")
    if data is not None:
        if choice == '1':     # create table
            create_table()
            continuee = input("Press Enter to continue...")
            print()
        elif choice == '2':   # drop table
            drop_table()
        elif choice == '3':   # insert user
            user_name = input("Enter user name: ")
            phone = input("Enter phone number: ")
            insert(user_name, phone)
        elif choice == '4':   # insert from csv
            csv_file_name = input("Enter csv file name without (.csv): ")
            insert_from_csv(csv_file_name=f"{csv_file_name}.csv")
        elif choice == '5':
            sub_choice = input("1. By first letter of name\n2. By provider\nEnter your choice: ")
            if sub_choice == '1':
                letter = input("Enter the first letter: ")
                letter = f"{letter}%"
                get_names_filter_by_letter(letter)
            elif sub_choice == '2':
                provider = input("Enter provider (e.g., Kcell, Beeline, Tele2): ")
                get_names_filter_by_provider(provider)
            else:
                print("Invalid sub-choice.")
            input("Press Enter to continue...")

        elif choice == '6':   # update user information
            choose = input("Choose one of the following:\n1. Update user name\n2. Update user phone\n")
            if choose == '1':
                update_user_name()
            elif choose == '2':
                update_user_phone()
            else:
                print("Invalid choice.")
        elif choice == '7':   # delete user
            name_or_phone = input("Enter user's phone: ")
            delete_user(name_or_phone)
            print("User deleted successfully.")
        elif choice == '8':   # show database
            print("Database:")
            for row in data:
                print(row)
            waiting = input("Press Enter to continue...")
            print()
        elif choice == '9':   # exit
            break
        else:
            print("Invalid choice. Please try again.")
    elif data is None and choice == '1':
            create_table()
    elif data is None and choice == '9':
        break
    else:
        print("Table does not exist. Please create a table first.")
        waiting = input("Press Enter to create Table...")
        create_table()

    data = select_all()

conn.close()