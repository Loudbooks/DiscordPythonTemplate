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

@client.command()
async def infoembed(ctx):
    await ctx.send("**First, to join the server, you must apply. Here is the link! https://forms.gle/3BES6WgUQmkM37do7** \nOnce you are done, ping a Server Owner to get access to the server.")
    embed=discord.Embed(title="**How to join the server!**", description="This is a Nation's SMP where you and your friends can gather resources, start wars and become the most powerful nation Minecraft has seen.  \n \nTo apply for the server, go to <#842013896519843841>. Once you have, ping a Server Owner is be whitelisted!   \n \nThe server IP is: **51.81.48.184:25585**  \n \nIf you have any questions, DM one of the staff!   Yours sincerely, The Ramen SMP Staff Team.", color=0xe60d43)
    await ctx.send(embed=embed)


load_dotenv()
TOKEN = os.getenv('TOKEN')
client.run(TOKEN)
