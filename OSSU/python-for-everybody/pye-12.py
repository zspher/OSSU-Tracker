# Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it can read any web page. You can use split('/') to break the URL into its component parts so you can extract the host name for the socket connect call. Add error checking using try and except to handle the condition where the user enters an improperly formatted or non-existent URL.
import sys
import socket

url = input("Enter a Url txt file: ")
try:
  website = url.split('/')[2]
  a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  a_socket.connect((website, 443))
  cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
  a_socket.send(cmd)
except:
  print("improperly formatted or non-existent URL")
  sys.exit()

while True:
  data = a_socket.recv(512)
  if len(data) < 1:
    break
  print(data.decode(), end='')

a_socket.close()

# Exercise 2: Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters. The program should retrieve the entire document and count the total number of characters and display the count of the number of characters at the end of the document.

import socket

url = input("Enter a Url txt file: ")
try:
  a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  website = url.split('/')[2]
  a_socket.connect((website, 80))
  cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
  a_socket.send(cmd)
except:
  print("improperly formatted or non-existent URL")
  sys.exit()

count = 0
while True:
  data = a_socket.recv(512)
  if len(data) < 1:
    break
  for char in data.decode():
    count += 1
    if count <= 3000:
      print(char, end='')
print('\n')
print(count)
a_socket.close()


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

# Exercise 4: Change the urllinks.py program to extract and count paragraph (p) tags from the retrieved HTML document and display the count of the paragraphs as the output of your program. Do not display the paragraph text, only count them. Test your program on several small web pages as well as some larger web pages.

import urllib.request, urllib.parse, urllib.error
import re
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
links = re.findall(b'(</p>)', html)
count = len(links)
print(count)

# Exercise 5: (Advanced) Change the socket program so that it only shows data after the headers and a blank line have been received. Remember that recv receives characters (newlines and all), not lines.
import sys
import socket

url = input("Enter a Url txt file: ")
try:
  website = url.split('/')[2]
  a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  a_socket.connect((website, 80))
  a_socket.send(f'GET {url} HTTP/1.0\r\n\r\n'.encode())
except:
  print("improperly formatted or non-existent URL")
  sys.exit()

file = b''
while True:
  data = a_socket.recv(512)
  if len(data) < 1: break
  file += data

a_socket.close()

pos = file.find(b'\r\n\r\n')
file = file[pos+4:].decode()
print(file)