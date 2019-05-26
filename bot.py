# Work with Python 3.6
import discord

TOKEN = 'NTgyMTI2OTY4MjAwMjMyOTYw.XOpTbw.D9sEHy1InuRriK0nWCMnFhdvhYQ'

client = discord.Client()

@client.event
async def on_message(message):
    if message.content == 'f':
        msg = '{0.author.message} has paid their respects.'.format(message)
        await client.send_message(message.channel, msg)
    if message.startswith('!p '):
        pun_handle(message.split(' '))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
