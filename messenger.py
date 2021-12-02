# import pyaztro
import songs
import random

def text():
  f = open("replies.txt", 'r')
  replies = eval(f.read())
  return replies


# def horoscope(name, star_sign='Aries'):
#   horo = pyaztro.Aztro(sign=star_sign.lower())
#   return "Always remember, " + name + " " + horo.description


def reply(emotion, name, singer):
  replies = text()
  fallback = "I'm afraid I don't have an intel about that."
  link = songs.song(emotion, singer)
  try:
    return random.choice(replies[emotion]) + " " + link
  except:
    return fallback
