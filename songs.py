import urllib.request
import re
import random

def ytlink(query):
  words = query.split(" ")
  new = list(map(lambda st: str.replace(st, " ", "+"), words))
  fin = 'https://www.youtube.com/results?search_query='+ "".join(new)
  html = urllib.request.urlopen(fin)
  video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
  select = random.choice(video_ids[:6])
  link = "https://www.youtube.com/watch?v=" + select
  return link

def song(emotion, singer):
  print(singer, emotion)
  lk = ytlink(emotion + " " + singer + " songs")
  return lk

