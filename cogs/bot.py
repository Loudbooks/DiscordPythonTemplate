import discord
from discord.ext import commands

class Bot(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print('COG is loaded.')

    #Commands go below
    @commands.command()
    async def jayden(self, ctx):
        await ctx.send('Jayden is currently active!')

def setup(client):
    client.add_cog(Bot(client))