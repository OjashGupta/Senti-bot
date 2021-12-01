import os
import discord
import random
import environ
import sentiment
import messenger
from alive import keep_alive

# reading .env file
env = environ.Env()
environ.Env.read_env()

Token=env("token")

client = discord.Client() 

@client.event
async def on_ready():
    print('We have logged in as .{0.user}'.format(client))

global status
status = False

@client.event
async def on_message(message):
  if not status:
    await message.channel.send("Hello! To get to know you better, I would like to get some information about yourself. Can you tell me your name?")
    name = message.content
    await message.channel.send("Nice to meet you, " + name +". Who is your favourite singer?")
    singer = message.content
    await message.channel.send("Do you believe in horoscopes?")
    nod = message.content
    star_sign = ''
    if "yes" in nod.lower():
      await message.channel.send("What is your star sign?")
      star_sign = message.content
    await message.channel.send("Thank you for the information. Now, tell me about your day.")
  else:
    if "bye" not in message.content.lower():
      emotion = sentiment.mood(message.content.lower())
      message.channel.send(messenger.reply(emotion, name, singer))
    else:
      await message.channel.send("Bye! Have a nice day!")
      await message.channel.send(messenger.horoscope(name, star_sign))




  
keep_alive() 
client.run(Token) 