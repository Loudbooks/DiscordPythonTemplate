import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
client = commands.Bot(command_prefix = '!')
client.remove_command('help')

noperms = 'You dont have permission to do this!'


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="!help for more info!"))
    print ('Bot is ready!')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')



@client.command()
async def help(ctx):
    await ctx.send('')
    
@client.command()
async def load(ctx, extention):
    if ctx.message.author.guild_permissions.manage_messages:
        client.load_extension(f'cogs.{extention}')
        await ctx.send('Loaded module')

@client.command()
async def unload(ctx, extention):
    if ctx.message.author.guild_permissions.manage_messages:
        client.unload_extension(f'cogs.{extention}')
        await ctx.send('Unloaded module.')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')



load_dotenv()
TOKEN = os.getenv('TOKEN')
client.run(TOKEN)
