from threading import Thread, Lock
from download_videos import YoutubeDownloader as yt
import os
import re
import time
from random import randint
from pytube import YouTube

with open("src/video_url.txt", "r") as f:
    video_list = eval(f.read())


def download_all_videos(urllist, downloadpath=None):
    """Downloads videos one by one in downloadpath directory"""
    # for url in urllist:
    # lock = Lock()
    # lock.acquire()
    aa = YouTube(urllist).streams.first().download(downloadpath)
    # print (aa.split("\")[1])
    print(f"Video {urllist} downloaded successfully.")

    # lock.release()
    # time.sleep(0.5)
    b = Thread(target=correct_file_names, args=(
        "C:\download-youtube-videos\download", aa.split('\\')[1]), name=f"rn-thread-{i}")
    b.start()

def correct_file_names(dirname, file):
    """delete a part of filename and correct naming like '1. *mp4'"""
    regex = re.compile("(p\d{,2})$")
    os.chdir("C:\download-youtube-videos\download")
    # for file in os.listdir(dirname):
    stext = os.path.splitext(file)
    getendpart = re.findall(regex, stext[0])
    if getendpart:
        newname = re.sub(getendpart[0], "", stext[0])
        print(f"{getendpart[0][1:]}. {newname.strip()}{stext[1]}")
        os.rename(
            file, f"{getendpart[0][1:]}. {newname.strip()}{stext[1]}")

starttime = time.time()
# Download in separate threads
for i in video_list:
    a = Thread(target=download_all_videos, args=(i, "download"), name=f"download-thread-{i}")
    a.start()

# for i in video_list:
#     download_all_videos(i, "download")

a.join()
# b.join()
print(time.time() - starttime)




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
