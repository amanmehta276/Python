from pytube import YouTube
from sys import argv

link=argv[1]
yt=YouTube(link)

print("Tiele: ",yt.title)
print("Views: ",yt.views)

yd=yt.streams.get_highest_resolution()
yd.download("https://www.youtube.com/watch?v=VIDEO_ID")

print("Download completed")