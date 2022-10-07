from socket import *
from time import *
import os
 
start_time = time()
HOST = '127.0.0.1'
PORT = 9999

client = socket(AF_INET, SOCK_STREAM)
client.connect((HOST, PORT))

song = input("Enter the song you want to download. \nHere: ")
sent = song.encode()
client.send(sent)


#----------寫入音樂檔----------------
while True:
    data = client.recv(1024)
    if not data: break
    path = '../NewMusicFile/'+ song +'.mp3'
    with open(path, 'ab') as f: 
        f.write(data)


#---------結算時間-----------------

file_size = os.path.getsize(path)
client.close()

print('連接已關閉')
end_time = time()
All_time = end_time - start_time

print("服務器已經運行 " + str(round(All_time, 1)) +" s")
print("該文件 " + str(round(file_size/1024/1024, 2)) + " mb")

