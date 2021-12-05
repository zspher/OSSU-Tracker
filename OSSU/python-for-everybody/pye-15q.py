# Q1
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

# import sqlite3

# con = sqlite3.connect('db.sqlite')
# cur = con.cursor()

# cur.execute("drop table if exists Ages")

# cur.execute("""
#   CREATE TABLE Ages ( 
#     name VARCHAR(128), 
#     age INTEGER
#   )
# """)

# cur.execute("DELETE FROM Ages;")
# cur.execute("INSERT INTO Ages (name, age) VALUES ('Rameesah', 16);")
# cur.execute("INSERT INTO Ages (name, age) VALUES ('Safa', 17);")
# cur.execute("INSERT INTO Ages (name, age) VALUES ('Orlaidh', 34);")
# cur.execute("INSERT INTO Ages (name, age) VALUES ('Eimantas', 23);")

# cur.execute("SELECT hex(name || age) AS X FROM Ages ORDER BY X")
# print(cur.fetchall()[0][0])
# con.close()

# Q2
# This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

# CREATE TABLE Counts (org TEXT, count INTEGER)
# When you have run the program on mbox.txt upload the resulting database file above for grading.
# If you run the program multiple times in testing or with dfferent files, make sure to empty out the data before each run.

# You can use this code as a starting point for your application: http://www.py4e.com/code3/emaildb.py.

# The data file for this application is the same as in previous assignments: http://www.py4e.com/code3/mbox.txt.

# Because the sample code is using an UPDATE statement and committing the results to the database as each record is read in the loop, it might take as long as a few minutes to process all the data. The commit insists on completely writing all the data to disk every time it is called.

# The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program, there is a balance between the number of operations you execute between commits and the importance of not losing the results of operations that have not yet been committed.

# * open files *
# * use regex on file | if match add to variable
# * add variable to database

import sqlite3

con = sqlite3.connect("db.sqlite")
cur = con.cursor()

cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

with open("mbox.txt", "r") as f:
  for line in f:
    if line.startswith("From "):
      org = line.split() 
      org = org[1]
      start = org.find("@")
      org = org[start+1:]
      cur.execute("SELECT count FROM Counts WHERE org = ? LIMIT 1", (org, ) )
      try:
        count = cur.fetchone()[0]
        cur.execute("UPDATE Counts SET count = ? WHERE org = ?", (count+1, org))
      except:
        cur.execute("INSERT INTO Counts (org, count) VALUES (?, ?)", (org, 1))
# v2
#       cur.execute("SELECT count FROM Counts WHERE org = ? LIMIT 1", (org, ) )
#       count = cur.fetchone()
#       if count is None:
#         cur.execute("INSERT INTO Counts (org, count) VALUES (?, ?)", (org, 1))
#       else:
#         cur.execute("UPDATE Counts SET count = count+1 WHERE org = ?", (org, ))

con.commit()
con.close()
