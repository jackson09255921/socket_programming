import socket
import sys

HOST = '127.0.0.1'
PORT = 8000


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print('Connect Success!!')

while True:    
    clientMessage = input("Give your question below.(Push enter to quit.)\n Here: ")
    client.sendall(clientMessage.encode())
    if clientMessage =='':
        client.close()
        sys.exit()

    serverMessage = str(client.recv(1024), encoding='utf-8')
    print('---------------\n Server:'+ serverMessage)

