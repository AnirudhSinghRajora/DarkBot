import discord
from discord.ext import commands,tasks
import os

token = 'Nzk1Mjk1MDQxMDk3Njk1MjYy.GMdfop.DKryJID2II1Xv5C6E35DtTG9eTRf3Wuu_R7uck'
bot = commands.Bot(command_prefix="$")


@bot.command()
async def Lol(ctx):
    await ctx.send("Really?")
    
    
for i in os.listdir('./cogs'):
	if i.endswith(".py"):
		bot.load_extension(f"cogs.{i[:-3]}")

bot.run(token)
