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