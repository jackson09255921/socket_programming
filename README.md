# socket_programming
A simple TCP/IP Music Player

## Introduction
哈囉~歡迎來使用燄嵐自製的音樂撥放器
由於影片似乎無法錄製到筆電本身的喇叭
小弟我就從這裡來簡單論述功能
若有任何疑問 歡迎告訴我
---
### Download_Process
檔案中含有四個檔案
1. musicGetter是用來從YT上取音樂檔
1. musicFileChange可以將上一個匯出的.mp4轉.mp3
  (如果覺得畫面而增加容量部會在意的話可以不用使用喔)
1. 其餘兩個.txt則是用來下載音樂的YT連結

---
### Client2Server & Server2Client
1. 顧名思義，一個是從客戶端載到伺服端，另一個則相反
1. 目前只有server to client可以進行自選音樂，若想要
   使用另一個可能就要自己微調一下喔~
c1. 下載完的音樂會同一收納到NewMusicFile中

---
### 音樂撥放器musicPlayer:
1. 就是用來撥放的程式
1. 記得在啟動撥放之前要先從本地端載入音樂喔~
1. 暫停按鍵似乎有點問題，如果有好心人可以順便幫小弟我
   調整一下
 
