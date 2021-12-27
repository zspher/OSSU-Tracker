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
