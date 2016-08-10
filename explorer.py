import psycopg2
from sys import argv
# Connect to db and open cursor
conn = psycopg2.connect("dbname=players user=tmendez")
cur = conn.cursor()

columns = ["name", "race", "class", "level"]

# TODO Insert | Display Table


def insert():
    name = input("Please enter the character's name: ")
    race = input("Please input your character's race (D&D 5e please...): ")
    char_class = input("Please input your character's class (5e please..): ")
    level = int(input("Please input your character's level: "))
    for item in [name, race, char_class]:
        item.strip("(")
    cur.execute("INSERT INTO players (name, race, class, level) VALUES (%s, %s, %s, %s)", (name, race, char_class, level))


def display():
    cur.execute("SELECT * FROM players;")
    results = cur.fetchall()
    for item in results:
        print(item)


def search(column, query):
    # cur.execute("SELECT * FROM players WHERE %s = %s;", (column, query))
    if column in columns:
        cur.execute("SELECT * FROM players WHERE " + column + " = %s;", (query,))
    # cur.execute("SELECT * FROM players")
    results = cur.fetchall()
    for item in results:
        print(item)


def search_options():
    for idx, item in enumerate(columns):
        print(str(idx) + ") " + item)
    select = int(input("What would you like to search on? "))
    if select < 0 or select > 3:
        print("Please try again...")
        return search_options()
    else:
        print(columns[select])
        return columns[select]


def get_query():
    query = input("What would you like to search for? ")
    return query


def menu():
    for idx, item in enumerate(["search", "insert", "display", "exit"]):
        print(str(idx) + ") ", item)
    select = int(input("What would you like to do? "))
    return select


def arg_parser():
    if argv[1] == "--search":
        select = 0
    if argv[1] == "--insert":
        select = 1
    if argv[1] == "--display":
        select = 2
    if argv[1] == "--help" or argv[1] == "-h":
        print("explorer.py has 3 command line tools: --search, --insert, --display")
        select = 3
    return select


def main():
    print("Hello!")
    while True:
        if len(argv) < 2:
            select = menu()
        if len(argv) >= 2:
            select = arg_parser()
        if select == 0:
            column = search_options()
            query = get_query()
            search(column, query)
            if len(argv) != 1:
                break
        if select == 1:
            insert()
            if len(argv) != 1:
                break
        if select == 2:
            display()
            if len(argv) != 1:
                break
        if select == 3:
            break
    conn.commit()
    print("Goodbye!")

if __name__ == '__main__':
    main()


# Close communication with the database
cur.close()
conn.close()
