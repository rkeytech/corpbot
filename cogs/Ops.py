import discord
from discord.ext import commands


class Ops(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    # Create events with @commands.Cog.listener()

    # Commands
    # Create commands with @commands.command()
    @commands.command()
    async def op(self, ctx, name=None, time=None, place=None, *, desc="This is a simple corp operation"):
        guild = self.client.guilds[0]
        cat = discord.utils.get(guild.categories, name='OPs')
        name = name
        time = time
        place = place
        # Create a specific channel for the Operation
        chnl = await cat.create_text_channel(
            name=f"{name} op"
        )

        # Create message for pilots to react if interesting
        mbed = discord.Embed(
            title = f"{name.capitalize()} Operation",
            description = f"{desc}",
            color = discord.Color.dark_green()
        )
        mbed.set_footer(text="React to the message if you are interesting")
        msg = await chnl.send(embed=mbed)
        await msg.pin()

def setup(client):
    client.add_cog(Ops(client))
