import discord
from discord.ext import commands,tasks
import json
import urllib.request
import random
client = discord.Client()
token = 'Nzk1Mjk1MDQxMDk3Njk1MjYy.X_HSOQ.CAhkE9uOrM3UoAg5CZN4QSyrj-E'


@client.event
async def on_ready():
   automeme.start()
   print("bot is online")
@tasks.loop(minutes=10)
async def automeme():
    
    url = "https://meme-api.herokuapp.com/gimme/dankmemes"
    response = urllib.request.urlopen(url)      
    data = json.loads(response.read()) 
    img_url = data['url']   
    post_link = data['postLink']
    img_title = data['title']
    memebed = discord.Embed(title=img_title,url=img_url,color=random.randint(0,0xffffff))
    
    memebed.set_image(url=img_url)
    meme_channel = client.get_channel(796340227152805939)
    await meme_channel.send(embed=memebed)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('hello'):
        await message.channel.send('Hello!')
    elif message.content.lower().startswith('evil laugh'):
        await message.channel.send('https://tenor.com/view/the-grinch-evil-smile-creepy-smile-gif-7618321')
    
       
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Ninja is a pro'))
    automeme.start()



client.run(token)
