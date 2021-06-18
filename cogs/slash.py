import discord
import os
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from dotenv import load_dotenv
from discord_slash import SlashCommand
noperms = 'You dont have permission to do this, if you think this is a mistake, contact Loudbook!'
guild_ids = [put_guildid_here]

class Slash(commands.Cog):
    def __init__(self, client):
        self.client = client


    @cog_ext.cog_slash(name="Ping", description="Get the latency of the bot!", guild_ids=guild_ids)
    async def ping(self, ctx: SlashContext):
      await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')
   

def setup(client):
    client.add_cog(Slash(client))
