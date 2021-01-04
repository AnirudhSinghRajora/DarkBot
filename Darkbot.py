import discord
from discord.ext import commands
token = 'NzY1MDg3Mzc2OTQxOTA4MDA4.X4PtJQ.o4ww6_d4gWO_MlIWE7HJieGDq5w'
client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(token)