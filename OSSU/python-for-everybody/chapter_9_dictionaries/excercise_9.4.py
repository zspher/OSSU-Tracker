# Exercise 4: Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5

# Enter a file name: mbox.txt
# zqian@umich.edu 195
fname = input("Enter a file name: ")
file = open(fname)
emailHistogram = dict()
for line in file:
  if line.startswith("From "):
    words = line.split()
    word = words[1]
    emailHistogram[word] = emailHistogram.get(word,0) + 1
mostMessages = max(emailHistogram, key=emailHistogram.get)
print(mostMessages, emailHistogram[mostMessages])