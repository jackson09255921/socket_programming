from socket import *
from time import *
import os
 
start_time = time()
HOST = '127.0.0.1'
PORT = 9999

server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
print("正在監聽")

#---------嘗試連線------------------
while True:
    conn, addr = server.accept()
    if conn:
        print("連接到客戶端")
    else:
        print("未連接到任何客戶")

#--------寫入檔案-------------------
    while True:
        data = conn.recv(1024)
        if not data: break
        path = './NewMusicFile/6.mp3'

        with open(path, 'ab') as f: 
            f.write(data)

#-------結算各項數據-------------------
    file_size = os.path.getsize(path)
    conn.close()
    print('連接已關閉')
    end_time = time()
    All_time = end_time - start_time

    print("服務器已經運行 " + str(round(All_time, 1)) +" s")
    print("該文件 " + str(round(file_size/1024/1024, 2)) + " mb")

    break