# download youtube videos
from pytube import YouTube
from requests_html import HTMLSession
import os
import re
import time


class YoutubeDownloader:
    """
    class to fetch all links from the youtube page and download the videos
    """
    @staticmethod
    def download_all_videos(urllist=[], downloadpath=None):
        """Downloads videos one by one in downloadpath directory"""
        for url in urllist:
            YouTube(url).streams.first().download(downloadpath)
            print(f"Video {url} downloaded successfully.")

    @staticmethod
    def correct_file_names(dirname):
        """delete a part of filename and correct naming like '1. *mp4'"""
        regex = re.compile("(p\d{,2})$")
        os.chdir("C:\download-youtube-videos\download")
        for file in os.listdir(dirname):
            stext = os.path.splitext(file)
            getendpart = re.findall(regex, stext[0])
            if getendpart:
                newname = re.sub(getendpart[0], "", stext[0])
                print(f"{getendpart[0][1:]}. {newname.strip()}{stext[1]}")
                os.rename(
                    file, f"{getendpart[0][1:]}. {newname.strip()}{stext[1]}")


    @staticmethod
    def get_video_length(dirname):
        """not completed"""
        os.chdir(os.path.join(os.curdir, "download"))
        for file in os.listdir(dirname):
            print (os.stat(file))

    @staticmethod
    def get_all_urls(url):
        r = HTMLSession().get(url)
        r.html.render()
        return r.html.absolute_links

starttime = time.time()
obj_u = YoutubeDownloader()
with open("src/video_url.txt", "r") as f:
    video_list = eval(f.read())


obj_u.download_all_videos(video_list, "download")
obj_u.correct_file_names("C:\download-youtube-videos\download")
# obj_u.get_video_length("C:\download-youtube-videos\download")
print(time.time() - starttime)
