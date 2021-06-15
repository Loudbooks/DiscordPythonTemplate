import discord
from discord.ext import commands

class Bot(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')

    #Commands go below
    @commands.command()
    async def ping1(self, ctx):
        await ctx.send('Pong!')

def setup(client):
    client.add_cog(Bot(client))