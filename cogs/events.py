import discord
from discord.ext import commands

class events(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def hi(self,ctx):
        await ctx.send("Hello!")
        
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'pong! {round(self.bot.latency * 1000)}ms')
        
def setup(bot):
    bot.add_cog(events(bot))