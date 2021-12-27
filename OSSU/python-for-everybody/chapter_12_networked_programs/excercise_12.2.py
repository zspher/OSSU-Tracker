# Exercise 2: Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters. The program should retrieve the entire document and count the total number of characters and display the count of the number of characters at the end of the document.

import sys
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


