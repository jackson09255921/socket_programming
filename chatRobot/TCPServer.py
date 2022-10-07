import socket
import sys

HOST = '127.0.0.1'
PORT = 8000

print('Ready to wait client connection.')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)
conn, addr = server.accept()
print('I found the client!')
print('Please waiting...')
while True:
    clientMessage = str(conn.recv(1024), encoding='utf-8')
    if clientMessage == '':
        conn.close()
        sys.exit()

    print('--------------\nClient message is:', clientMessage)
    serverMessage = input('Give your answer. \n Here: ')
    conn.sendall(serverMessage.encode())