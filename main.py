import os
import discord
import random
import environ
import sentiment
import messenger
from alive import keep_alive

# # reading .env file
# env = environ.Env()
# environ.Env.read_env()

Token= ""

client = discord.Client() 

@client.event
async def on_ready():
    print('We have logged in as .{0.user}'.format(client))


status = "name"

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  global status
  global name
  global singer
  if status == "name":
    await message.channel.send("Hello! To get to know you better, I would like to get some information about yourself. Can you tell me your name?") 
    status = "singer"
  elif status == "singer":
    name = str(message.content)
    await message.channel.send("Nice to meet you " + name + "! Who is your favourite singer?")
    status = "horo"
  elif status == "horo":
    singer = str(message.content)
    print(singer)
    await message.channel.send("Do you believe in horoscopes?")
    status = "talk"
  elif status == "talk":
    nod = str(message.content).lower()
    print(nod)
    star_sign = ''
    if nod.startswith("yes"):
      await message.channel.send("What is your star sign?")
    status = "end_survey"
  elif status == "end_survey":
      if nod.startswith("no"):
        star_sign = str(message.content)
      await message.channel.send("Thank you for the information. Now, tell me about your day.")
      status = "conversation"
  elif status == "conversation":
      emotion = sentiment.mood(str(message.content).lower())
      await message.channel.send(messenger.reply(emotion, name, singer))
      if message.content.startswith("$bye"):
        await message.channel.send("Bye! Have a nice day!")
        return
      # await message.channel.send(messenger.horoscope(name, star_sign))




  
keep_alive() 
client.run(Token) 