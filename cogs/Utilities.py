import discord
from discord.ext import commands
import csv


class Utilities(commands.Cog):
    def __init__(self, client):
        self.client = client

    def read_csv(self, filename):
        with open(filename, newline='') as f:
            rdr = csv.reader(f, delimiter=',')
            for row in rdr:
                print(row)
    # Events
    # Create events with @commands.Cog.listener()

    # Commands
    # Create commands with @commands.command()
    @commands.command()
    async def giveaway(self, ctx):
        self.read_csv('giveaways.csv')


def setup(client):
    client.add_cog(Utilities(client))
