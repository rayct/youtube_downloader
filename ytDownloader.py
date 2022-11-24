
# import pip install pytube
from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

# ADD FOLDER HERE
yd.download('./YT_DOWNLOADS')

# To run ths program type the following below into your command/terminal
# python3 youtube_downloader.py "NAME OF URL GOES HERE!"