import discord
from discord.ext import commands,tasks
import json
import urllib.request
import random
token = 'Nzk1Mjk1MDQxMDk3Njk1MjYy.X_HSOQ.CAhkE9uOrM3UoAg5CZN4QSyrj-E'
client = discord.Client()
@client.event
async def on_ready():
   automeme.start()
   print("bot is online")
@tasks.loop(minutes=3)
async def automeme():
    
    url = "https://meme-api.herokuapp.com/gimme/dankmemes"
    response = urllib.request.urlopen(url)      
    data = json.loads(response.read()) 
    img_url = data['url']   
    post_link = data['postLink']
    img_title = data['title']
    memebed = discord.Embed(title=img_title,url=img_url,color=random.randint(0,0xffffff))
    
    memebed.set_image(url=img_url)
    meme_channel = bot.get_channel(764758915292332032)
    await meme_channel.send(embed=memebed)

client.run(token)