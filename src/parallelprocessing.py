from threading import Thread
from download_videos import YoutubeDownloader as yt
import os
import time
from random import randint

with open("src/video_url.txt", "r") as f:
    video_list = eval(f.read())


# Download in separate threads
for i in video_list:
    a = Thread(target=yt.download_all_videos, args=(i,), name=f"download-thread-{i}")
    a.start()






"""
********************* practice parallel execution using files **************************
def temp(num):
    time.sleep(randint(5,10))
    print (f"new-{num}")
    os.system(f"echo '{num}' >> test{num}.txt")
    b = Thread(target=rn, args=(f"test{num}.txt",), name=f"rn-thread-{i}")
    b.start()

def rn(filename):
    time.sleep(1)
    os.rename(filename, filename + "akash")



for i in range(5):
    a = Thread(target=temp, args=(i,), name=f"download-thread-{i}")
    a.start()
"""
