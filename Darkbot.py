import discord
from discord.ext import commands
token = 'Nzk1Mjk1MDQxMDk3Njk1MjYy.X_HSOQ.CAhkE9uOrM3UoAg5CZN4QSyrj-E'
client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(token)
