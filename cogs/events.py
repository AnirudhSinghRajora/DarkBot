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
    @commands.command()
    async def evil(self,ctx):
        await ctx.send("https://tenor.com/view/the-grinch-evil-smile-creepy-smile-gif-7618321")


    @commands.command()
    async def abe_saale(self,ctx):
        await ctx.send("https://tenor.com/view/abe-saale-sabbir31x-harmonium-sale-gif-15727715")
        
def setup(bot):
    bot.add_cog(events(bot))
