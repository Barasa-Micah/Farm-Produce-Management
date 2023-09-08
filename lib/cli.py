import sqlite3
import argparse


def create_database(database_name):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()


    cursor.execute('''CREATE TABLE IF NOT EXISTS data (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT
    )''')

   
    cursor.execute('''CREATE TABLE IF NOT EXISTS farm_products (
        id INTEGER PRIMARY KEY,
        product_name TEXT,
        quantity INTEGER
    )''')

    connection.commit()
    connection.close()

def add_data(database_name, name, description):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO data (name, description) VALUES (?, ?)", (name, description))
    connection.commit()
    connection.close()

def add_farm_product(database_name, product_name, quantity):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO farm_products (product_name, quantity) VALUES (?, ?)", (product_name, quantity))
    connection.commit()
    connection.close()


def sort_farmers_needs():
    print("Sorting farmers' needs")


def sort_consumers_needs():
    print("Sorting consumers' needs")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Farm Data Management CLI")
    parser.add_argument("--database", required=True, help="Database name")
    parser.add_argument("command", choices=["add_data", "add_product", "sort_farmers", "sort_consumers"], help="Command to execute")

    args = parser.parse_args()

   
    create_database(args.database)

    if args.command == "add_data":
        name = input("Enter name: ")
        description = input("Enter description: ")
        add_data(args.database, name, description)
        print("Data added to the database.")
    elif args.command == "add_product":
        product_name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        add_farm_product(args.database, product_name, quantity)
        print("Farm product added to the database.")
    elif args.command == "sort_farmers":
        sort_farmers_needs()
    elif args.command == "sort_consumers":
        sort_consumers_needs()
