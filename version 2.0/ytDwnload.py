from pytube import YouTube
from os import getcwd, mkdir
from os.path import isdir
from sys import argv, exit

cur_dir: str = getcwd()
link: str
dir: str

try:
    mkdir(cur_dir + "\\audio")
except:
    pass

try:
    mkdir(cur_dir + "\\res")
except:
    pass

try:
    open(cur_dir + "\\res\\last.txt", mode='r', encoding='utf-8')
except FileNotFoundError:
    open(cur_dir + "\\res\\last.txt", mode='x', encoding='utf-8')


def get_name():
    with open(cur_dir + "\\res\\last.txt", mode='r', encoding='utf-8') as f:
        array = f.readlines()
        str_to_ret = array[0] + array[1]
        str_to_ret.replace("\n", "")
        return str_to_ret


if "--only_title" in argv:
    try: dir = argv[2]
    except IndexError: dir = ''
    link = get_name()
    try: 
        yt = YouTube(link)
        title = yt.title
        with open(cur_dir + "\\res\\last.txt", encoding='utf-8', mode="w") as file:
            file.write(title)
    except:
        with open(cur_dir + "\\res\\last.txt", encoding='utf-8', mode="w") as file:
                file.write(link)
    exit(0)

    
elif len(argv) == 2:
    dir = argv[1]


elif len(argv) == 1:
    dir = getcwd() + "\\audio"
link = get_name()
    

yt = YouTube(link)
title = yt.title
stream = yt.streams.filter(only_audio=True).first()
stream.download(output_path=dir, filename=title+".mp3")

#https://www.youtube.com/watch?v=a06wve-5PAo&list=RDut8nMaDen9E&index=6&ab_channel=CAKEBOY

#C:UsersUserPycharmProjectsConCenter>pyinstaller ytDwnload.py --onefile -n=engine.exe
