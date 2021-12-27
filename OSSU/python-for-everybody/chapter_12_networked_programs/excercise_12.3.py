# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, (2) displaying up to 3000 characters, and (3) counting the overall number of characters in the document. Don’t worry about the headers for this exercise, simply show the first 3000 characters of the document contents.

import urllib.request 
import sys

url = input("Enter a Url txt file: ")
try:
  data = urllib.request.urlopen(url)
except:
  print('improperly formatted or non-existent URL')
  sys.exit()


count = 0
for line in data:
  for char in line.decode():
    count += 1
    if count <= 3000:
      print(char, end='')
print('\n')
print(count) 