import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

class Jayden(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print('Jayden machine is loaded.')

    #Commands go below


def setup(client):
    client.add_cog(Jayden(client))