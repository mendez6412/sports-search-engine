import psycopg2
import csv

# Connect to an existing database
conn = psycopg2.connect("dbname=players user=tmendez")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute("DROP TABLE players")
cur.execute("CREATE TABLE IF NOT EXISTS players (id serial PRIMARY KEY, name varchar, race varchar, class varchar, level integer);")

with open('classes.csv') as f:
    reader = csv.reader(f)
    headers = next(reader)
    for row in reader:
        cur.execute("INSERT INTO players (name, race, class, level) VALUES (%s, %s, %s, %s)", (row[0], row[1], row[2], row[3]))

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()
