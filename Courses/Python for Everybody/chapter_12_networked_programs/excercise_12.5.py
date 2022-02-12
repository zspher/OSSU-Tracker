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