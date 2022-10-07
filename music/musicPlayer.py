import os
import time
import tkinter
import tkinter.filedialog
import threading
import pygame

# 定義一些變數
folder = '' #歌曲資料夾路徑
res = [] #存放歌曲路徑
ret = [] #存放歌曲名稱
num = 0
now_music = ''
one_start = True

# 功能
# 新增檔案
def buttonChooseFile():
    global folder
    global res
    global ret
    folder = tkinter.filedialog.askdirectory()
    if folder:
        musics = [folder + '\\' + music
                  for music in os.listdir(folder)\
    \
                  if music.endswith(('.mp3','.m4a','.wav','.ogg'))]
        for i in musics:
            ret.append(i.split('\\')[1:])
            res.append(i.replace('\\','/'))
        var2 = tkinter.StringVar()
        var2.set(ret)
        global lb
        lb = tkinter.Listbox(root,listvariable=var2)

        lb.place(x=50,y=150,width=260,height=300)
    if not folder:
        return
    global playing
    playing = True

    # 根據情況禁用和啓用相應的按鈕
    button_play['state'] = 'normal'
    button_delete['state'] = 'normal'
    voice_bar['state'] = 'normal'
    pause_resume.set('播放')

# 刪除音樂
def buttonDeleteClick():
    music = lb.get('active')[0]
    list_temp = [music]
    ret.remove(list_temp)
    for i in res:
        if i.split("/")[-1] == music:
            res.remove(i)
    lb.delete('active')

# 播放音樂
def play():
    global one_start
    if len(res):
        # 初始化
        pygame.mixer.init()
        global num
        while playing:
            if not pygame.mixer.music.get_busy():
                nextMusic = res[num]
                if one_start:
                    # 播放選中的那首歌
                    nextMusic = lb.get('active')
                    temp_list = [nextMusic[0]]
                    current_index = ret.index(temp_list)
                    num = current_index
                    nextMusic = res[current_index]
                print(num)
                pygame.mixer.music.load(nextMusic.encode())
                # 播放一次
                pygame.mixer.music.play(1)

                # print(len(res)-1)
                if len(res) - 1 == num:
                    num = 0
                else:
                    num = num + 1
                nextMusic = nextMusic.split('/')[-1]
                play_state.set('playing...')
                musicName.set(nextMusic)
                one_start = False
            else:
                time.sleep(0.1)

# 點選播放
def buttonPlayClick():
    button_next['state'] = 'normal'
    button_prev['state'] = 'normal'
    # 選擇要播放的音樂資料夾
    if pause_resume.get() == '播放':
        pause_resume.set('暫停')
        play_state.set('playing...')
        global folder
        if not folder:
            folder = tkinter.filedialog.askdirectory()
        if not folder:
            return
        global playing
        playing = True
        # 建立一個執行緒來播放音樂，當前主執行緒用來接收使用者操作
        t = threading.Thread(target=play)
        t.start()
    elif pause_resume.get() == '暫停':
        # pygame.mixer.init()
        pygame.mixer.music.pause()
        pause_resume.set("繼續")
        play_state.set('paused...')
    elif pause_resume.get() == '繼續':
        # pygame.mixer.init()
        pygame.mixer.music.unpause()
        pause_resume.set('暫停')
        play_state.set('playing...')

# 上一首
def buttonPrevClick():
    global playing
    playing = False
    pygame.mixer.init()
    pygame.mixer.music.stop()
    global num
    if num == 0:
        num = len(res) - 2
    elif num == len(res) - 1:
        num -= 2
    else:
        num -= 2
    print(num)
    playing = True
    # 建立執行緒播放音樂
    t = threading.Thread(target=play)
    t.start()

# 下一首
def buttonNextClick():
    global playing
    playing = False
    pygame.mixer.music.stop()
    global num
    if len(res) == num:
        num = 0
    playing = True
    # 建立執行緒播放音樂
    t = threading.Thread(target=play)
    t.start()

# 關閉視窗
def closeWindow():
    global playing
    playing = False
    time.sleep(0.3)
    try:
        # 停止播放，如果已經停止
        # 再次停止時會拋出異常，所以需要異常捕獲
        pygame.mixer.music.stop()
        pygame.mixer.quit()
    except:
        pass
    root.destroy() # 整個介面退出

# 音量控制，預設是一半的音量值
def control_voice(value=0.5):
    try:
        pygame.mixer.music.set_volume(float(value))
    except:
        pass

# 介面
root = tkinter.Tk()
root.title('音樂播放器')
root.geometry('460x600+500+100')
root.resizable(False,False)


# 視窗關閉
root.protocol("WM_DELETE_WINDOW",closeWindow)
# 新增檔案按鈕
button_choose = tkinter.Button(root,text='新增',command=buttonChooseFile)
button_choose.place(x=50,y=10,width=50,height=20)
# 刪除歌曲按鈕
button_delete = tkinter.Button(root,text='刪除',command=buttonDeleteClick)
button_delete.place(x=120,y=10,width=50,height=20)
button_delete['state'] = 'disabled'
# 可變字串元件
pause_resume = tkinter.StringVar(root,value='播放')
# 播放按鈕
button_play = tkinter.Button(root,textvariable=pause_resume,command=buttonPlayClick)
button_play.place(x=260,y=10,width=50,height=20)
button_play['state'] = 'disabled'
# 上一首
button_prev = tkinter.Button(root,text='上一首',command=buttonPrevClick)
button_prev.place(x=190,y=10,width=50,height=20)
button_prev['state'] = 'disabled'
# 下一首
button_next = tkinter.Button(root,text='下一首',command=buttonNextClick)
button_next.place(x=330,y=10,width=50,height=20)
button_next['state'] = 'disabled'
# 播放器狀態
play_state = tkinter.StringVar(root,value='暫時沒有播放音樂呢...')
stateLabel = tkinter.Label(root,textvariable=play_state,fg='green')
stateLabel.place(x=10,y=30,width=260,height=20)
# 當前播放的音樂
musicName = tkinter.StringVar(root,value='')
labelName = tkinter.Label(root,textvariable=musicName,font=("微軟雅黑", 12),fg='#008c8c')
labelName.place(x=10,y=500,width=400,height=30)
# font=("微軟雅黑", 20),  # 字型和大小
#                       fg='blue'
# 音量條
voice_bar = tkinter.Scale(root,label='音量',from_=0,to=1,orient=tkinter.HORIZONTAL,
                  length=240,showvalue=0.5,tickinterval=0.5,resolution=0.1,command=control_voice)
voice_bar.set(0.5)
voice_bar.place(x=50,y=50,width=200)
voice_bar['state'] = 'disabled'
# 進度條
# progress_bar = tkinter.Scale(root,from_=0,to=10,orient=tkinter.HORIZONTAL)
root.mainloop()