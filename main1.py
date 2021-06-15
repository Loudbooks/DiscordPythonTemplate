import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
client = commands.Bot(command_prefix = 'r!')




@client.event
async def on_message(message):
    if 'join' in message.content:
        if message.author == client.user:
            return
        print('Sending join message')
        await message.channel.send('**To join the server, type r!whitelist**')
    await client.process_commands(message)

@client.event
async def on_ready():
    print ('Bot is ready!')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def hello(ctx):
    await ctx.send('Why hello there good human!')



@client.command()
async def whitelist(ctx):
    await ctx.send("**First, to join the server, you must apply. Here is the link! https://forms.gle/3BES6WgUQmkM37do7** \nOnce you are done, ping a Server Owner to get access to the server.")

TOKEN = os.environ.get('TOKEN')

client.run('ODU0MTU2ODAyMzI1NDc5NDM0.YMf1gw._zr4rp7szfX_dWZuFZkfQODIxUw')
