import discord
from discord.ext import commands,tasks
import json
import urllib.request
import random
token = 'Nzk1Mjk1MDQxMDk3Njk1MjYy.X_HSOQ.CAhkE9uOrM3UoAg5CZN4QSyrj-E'


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
    
@client.event
async def on_ready():
   automeme.start()
   print("client is online")
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
    meme_channel = client.get_channel(764758915292332032)
    await meme_channel.send(embed=memebed)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('hello'):
        await message.channel.send('Hello!')
    elif message.content.lower().startswith('evil laugh'):
        await message.channel.send('https://tenor.com/view/the-grinch-evil-smile-creepy-smile-gif-7618321')
    elif message.content.lower().startswith('abe saale'):
        await message.channel.send('https://tenor.com/view/abe-saale-sabbir31x-harmonium-sale-gif-15727715')
    elif message.content.lower().startswith('mar saale ko'):
        await message.channel.send('https://tenor.com/view/moumita-khopdi-tod-re-saale-ka-pointing-gif-15226261')
       



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Ninja is Hattori Hazno!'))

client.run(token)
