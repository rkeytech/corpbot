import discord
from discord.ext import commands

class Utilities(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    # Create events with @commands.Cog.listener()

    # Commands
    # Create commands with @commands.command()
    @commands.command()
    async def giveaway(self, ctx):
        pass


def setup(client):
    client.add_cog(Utilities(client))