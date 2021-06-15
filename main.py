"""
import discord
TOKEN = 'ODU0MTU2ODAyMzI1NDc5NDM0.YMf1gw._zr4rp7szfX_dWZuFZkfQODIxUw'
PREFIX = '!'
INTENTS = discord.Intents.default()
client = discord.Client(commands_prefix=PREFIX, intents=INTENTS)


@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')


  if message.content.startswith('Bad bot'):
    await message.channel.send('Bad human')


@client.event()
async def ping(message):
    await message.channel.send(f'Pong! {round(client.latency * 1000)}ms')


client.run(TOKEN)
"""