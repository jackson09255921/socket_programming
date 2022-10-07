from moviepy.editor import *

for i in range(1, 44):
    filename='JapaneseSong' + str(i) + '.mp4'
    targetname='JapaneseSong' + str(i) + '.mp3'
    video=VideoFileClip(filename)
    video.audio.write_audiofile(targetname)