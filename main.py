import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
client = commands.Bot(command_prefix = 'r!')
client.remove_command('help')

noperms = 'You dont have permission to do this, if you think this is a mistake, contact Loudbook!'

@client.event
async def on_message(message):
    if 'join' in message.content:
        if message.author == client.user:
            return
        elif message.author.id == 845383239043514388:
            return
        else:
            print('Sending join message')
            await message.channel.send('**To join the server, type r!whitelist**')
            await client.process_commands(message)
@client.listen()
async def on_message(message):
    await client.process_commands(message)
    if 'bad bot' in message.content:
        if message.author == client.user:
            return
        await message.channel.send('bad human.')



@client.listen()
async def on_message(message):
    if 'join1' in message.content:
        print("in on_message #2")




@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="r!help for more info!"))
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
async def info(ctx):
    embed=discord.Embed(title="**How to join the server!**", description="This is a Nation's SMP where you and your friends can gather resources, start wars and become the most powerful nation Minecraft has seen.  \n \nTo apply for the server, go to <#842013896519843841>. Once you have, ping a Server Owner is be whitelisted!   \n \nThe server IP is: **51.81.48.184:25585**  \n \nIf you have any questions, DM one of the staff!   Yours sincerely, The Ramen SMP Staff Team.", color=0xe60d43)
    await ctx.send(embed=embed)

@client.command()
async def kick(ctx):
    if ctx.message.author.guild_permissions.administrator:
        await ctx.send("Test")
    else:
        await ctx.send(noperms)

@client.command()
async def help(ctx):
    await ctx.send('**Current Command List:** \n`r!help` - Shows this menu. \n`r!info` - Gives info on how to join the smp. \n`r!whitelist` - Shows how to apply for the server. \n`r!ping` - Shows the ping in ms to the server. \n`r!purge <amount>` - Deleted the specified number of messages. **Default is 50**. \n`r!hello` - Replies with a warm hello! \n`r!load <cog>` - Loads a COG module.')

@client.command()
async def load(ctx, extention):
    if ctx.message.author.guild_permissions.manage_messages:
        client.load_extension(f'cogs.{extention}')
        await ctx.send('Loaded Jayden module')

@client.command()
async def unload(ctx, extention):
    if ctx.message.author.guild_permissions.manage_messages:
        client.unload_extension(f'cogs.{extention}')
        await ctx.send('Unloaded Jayden module.')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
async def purge(ctx, amount=50):
    if ctx.message.author.guild_permissions.manage_messages:
        await ctx.channel.purge(limit=amount+1)

        

    else:
        await ctx.send(noperms)

load_dotenv()
TOKEN = os.getenv('TOKEN')
client.run(TOKEN)
