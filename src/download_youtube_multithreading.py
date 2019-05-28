# import modules
from requests import get
from threading import Thread, Lock
import os
import re
import time
from pytube import YouTube
from concurrent.futures import ThreadPoolExecutor



class DownloadYoutubeVideos:
    """
    Class for downloading youtube videos in parallel using pytube and threading module
    """

    def __init__(self):
        """ initialization method """
        pass

    def get_video_url_from_playlist(self, main_url):
        """ get all video url from playlist """
        response = get(url=main_url, timeout=5)
        return response.text

    def download_youtube_videos(self, single_url, downloadpath="download"):
        """ download single video at a time """
        return YouTube(single_url).streams.first().download(downloadpath)

    def download_in_parallel(self, url_list):
        """ Download video concurrently using ThreadPoolExecutor """
        with ThreadPoolExecutor(max_workers = 6) as executor:
            return executor.map(self.download_youtube_videos, url_list)



# Main
with open("video_url_data_analysis.txt", "r") as f:
    url_list = eval(f.read())
print(url_list)
a = DownloadYoutubeVideos()
print (a.download_in_parallel(url_list))

