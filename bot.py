# Work with Python 3.6
import discord
import point_counter as pc

TOKEN = "This isn't supposed to be shared."

client = discord.Client()

print('Starting point counter...')
point_counter = pc.Point_Counter("data.dat")
print('Done.')

@client.event
async def on_message(message):
    if message.content == 'f':
        msg = '{0.author.mention} has paid their respects.'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!p'):
        print("Point Counter message recieved.")
        msg = point_counter.handle(message.content)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
