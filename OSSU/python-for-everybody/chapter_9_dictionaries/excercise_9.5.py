# Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
fname = input("Enter a file name: ")
file = open(fname)
emailHistogram = dict()
for line in file:
  if line.startswith("From "):
    words = line.split()
    word = words[1]
    start = word.find('@')
    word = word[start+1:]
    emailHistogram[word] = emailHistogram.get(word,0) + 1
print(emailHistogram)