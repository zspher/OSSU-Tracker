# Then, create a SQLITE database or use an existing database and create a table in the database called "Ages":

# CREATE TABLE Ages ( 
#   name VARCHAR(128), 
#   age INTEGER
# )
# Then make sure the table is empty by deleting any rows that you previously inserted, and insert these rows and only these rows with the following commands:

# DELETE FROM Ages;
# INSERT INTO Ages (name, age) VALUES ('Rameesah', 16);
# INSERT INTO Ages (name, age) VALUES ('Safa', 17);
# INSERT INTO Ages (name, age) VALUES ('Orlaidh', 34);
# INSERT INTO Ages (name, age) VALUES ('Eimantas', 23);
# Once the inserts are done, run the following SQL command:
# SELECT hex(name || age) AS X FROM Ages ORDER BY X
# Find the first row in the resulting record set and enter the long string that looks like 53656C696E613333.

import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.execute("drop table if exists Ages")

cur.execute("""
  CREATE TABLE Ages ( 
    name VARCHAR(128), 
    age INTEGER
  )
""")

cur.execute("DELETE FROM Ages;")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Rameesah', 16);")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Safa', 17);")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Orlaidh', 34);")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Eimantas', 23);")

cur.execute("SELECT hex(name || age) AS X FROM Ages ORDER BY X")
print(cur.fetchall()[0][0])
con.close()