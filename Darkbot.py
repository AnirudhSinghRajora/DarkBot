import discord

TOKEN = 'NzY1MDg3Mzc2OTQxOTA4MDA4.X4PtJQ.o4ww6_d4gWO_MlIWE7HJieGDq5w'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    
client.run(TOKEN)