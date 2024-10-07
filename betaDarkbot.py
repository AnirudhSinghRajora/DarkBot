import discord
from discord.ext import commands,tasks
import os

token = ''
bot = commands.Bot(command_prefix="$")


@bot.command()
async def Lol(ctx):
    await ctx.send("Really?")
    
    
for i in os.listdir('./cogs'):
	if i.endswith(".py"):
		bot.load_extension(f"cogs.{i[:-3]}")

bot.run(token)
