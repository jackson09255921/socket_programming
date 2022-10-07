from socket import *
import os 
from time import *

HOST = '127.0.0.1'
PORT = 9999


server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
print("正在監聽")

#---------------等待連接-----------------------
while True:
    conn, addr = server.accept()
    if conn:
        print("連接到客戶端")
    else:
        print("未連接到任何客戶")
    song = conn.recv(1024)
    song = song.decode()
    path = 'D:/schoolwork/一般課業/大三上/計算機網路/socket_programming/music_file3/JapaneseSong'+ song +'.mp3'
    # path = 'D:/schoolwork/一般課業/大三上/計算機網路/socket_programming/music_file3/JapaneseSong1.mp3'

#---------------讀取檔案---------------------
    with open(path, 'rb') as f: 
        message = f.read()
    file_size = os.path.getsize(path) / 1024 / 1024

#---------------發送檔案-----------------
    start_time = time()
    conn.send(message)
    end_time = time()

#---------------結算時間---------------------
    print("文件已發送")
    conn.close()
    break

print('連接關閉')