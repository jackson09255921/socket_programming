# coding: utf-8
from pytube import YouTube
from moviepy.editor import *

if __name__ == "__main__":
    # Init
    f = open('download2.txt')
    for url in f.readlines():
        yt = YouTube(url)
        video = yt.streams.filter().get_highest_resolution().download('../music_file4')
    f.close
