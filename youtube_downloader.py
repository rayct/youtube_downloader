
# import pip install pytube
from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

# ADD FOLDER HERE
yd.download('./FOLDERNAME')

# Run this Command to run the program
# python3 youtube_downloader.py "NAME OF URL GOES HERE!"