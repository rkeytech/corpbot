import discord
from discord.ext import commands
import csv


class Utilities(commands.Cog):
    def __init__(self, client):
        self.client = client

    def read_csv(self, filename):
        items = []
        with open(filename, newline='') as f:
            rdr = csv.reader(f, delimiter=',')
            for row in rdr:
                items.append((row[0], row[-1],))
        return items

    # Events
    # Create events with @commands.Cog.listener()

    # Commands
    # Create commands with @commands.command()
    @commands.command()
    async def giveaway(self, ctx, loot='giveaways.csv'):
        giveaway_items = self.read_csv(loot)
        print(giveaway_items)


def setup(client):
    client.add_cog(Utilities(client))
