from socket import *
import os 
from time import *

HOST = '127.0.0.1'
PORT = 9999

path = 'D:/schoolwork/一般課業/大三上/計算機網路/socket_programming/music_file3/JapaneseSong1.mp3'


#-------------讀取檔案---------------------
with open(path, 'rb') as f: 
    message = f.read()

file_size = os.path.getsize(path) / 1024 / 1024

#--------------客戶端連線------------------
client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 9999))



print("已連接")

#------------發送時間--------------------
start_time = time()
client.send(message)
end_time = time()

#-------------總時間結算---------------------
All_time = end_time - start_time
rate = round(file_size / All_time, 2)
print("文件已發送")

client.close()



print('連接關閉')