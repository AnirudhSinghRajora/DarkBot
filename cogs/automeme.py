import discord
from discord.ext import commands,tasks
import json
import urllib.request
import random
import requests 
class automeme(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.requests = requests
        
    @commands.Cog.listener()
    async def on_ready(self): 
    	print("online.")
    	await self.bot.change_presence(activity=discord.Game('Minecraft is Op'))
    	self.automeme.start()
   
    
    @tasks.loop(minutes=10)
    async def automeme(self):
        req = self.requests.get("https://meme-api.herokuapp.com/gimme")
        img_title = req.json()["title"]
        img_url = req.json()["url"]
        
        em = discord.Embed(
            title=img_title,
            url=img_url,
            color=discord.Color.random())
        em.set_image(url=img_url)
        
        chnl = self.bot.get_channel(796340227152805939) 
        await chnl.send(embed=em)




def setup(bot):
    bot.add_cog(automeme(bot))
