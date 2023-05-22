from pytube import YouTube
from os import getcwd, mkdir
from os.path import isdir, isfile
if not isdir("\\audio"): mkdir("\\audio")
if not isdir("\\res"): mkdir("\\res")
if not isfile("\\res\\last.txt"):
    with open("\\res\\last.txt", encoding='utf-8', mode="w") as file:
        file.write("")

link = input("Link-->: ")
yt = YouTube(link)
title = yt.title
stream = yt.streams.filter(only_audio=True).first()
stream.download(output_path=getcwd() + "\\audio", filename=title+".mp3")
print("DONE!!!")
