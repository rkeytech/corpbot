import discord
from discord.ext import commands
import csv
from random import choice


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
    async def giveaway(self, ctx, name='Just'):
        guild = self.client.guilds[0]
        cat = discord.utils.get(guild.categories, name='Giveaways')
        member = ctx.message.author
        mbed = discord.Embed(
            name=f"{name} GIVEAWAY".upper(),
            description=f"This is a {name} giveaway so we can share with you \
                something back, for all your troubles and for being \
                nice and active pilots.",
            color=discord.Colour.dark_gold()
        )
        mbed.set_author(name=member.nick, icon_url=member.avatar_url)
        mbed.add_field(
            name='__How To participate__',
            value="In order to participate in our giveaway the only thing you \
                have to do is to react to this message. You can react with \
                any emoticon you like. It doesn't matter. Or doed it? :)",
            inline=False
        )
        mbed.set_footer(text=f"code:{member.id}")

        # Processing the giveaway
        g_channel = await cat.create_text_channel(name=f"{name} giveaway")
        await g_channel.set_permissions(member, send_messages=True)

        msg = await g_channel.send(embed=mbed)
        await msg.pin()

    @commands.command()
    async def endg(self, ctx, loot=None):
        if ctx.message.channel.category.name == 'Giveaways':
            giveaway_items = ''
            if loot:
                giveaway_items = self.read_csv(f'./assets/{loot}.csv')
            pilots = set()
            pinned = await ctx.message.channel.pins()
            msg = await ctx.message.channel.fetch_message(pinned[0].id)
            owner_id = msg.embeds[-1].footer.text.split(':').strip()
            if owner_id == str(ctx.message.author.id):
                for reaction in msg.reactions:
                    users = await reaction.users().flatten()
                    pilots.update(users)
                winner = choice(pilots)
                if giveaway_items:
                    w_item = choice(giveaway_items)
                else:
                    w_item = 'this giveaway'
                await ctx.message.channel.send(
                    f"_**{winner.nick}**_ _is the winner for_ \
                    _**{w_item}**_ _!!_"
                )
                await winner.send(
                    f"You are the winner of the _**\
                    {ctx.message.channel.name.split('-')[0]}\
                    **_ giveaway! Congratulation!!"
                )
            else:
                await ctx.message.channel.send(
                    "You are not the owner of this giveaway!!"
                )
        else:
            await ctx.message.channel.send(
                "You must be in a giveaway channel to end the giveaway!"
            )


def setup(client):
    client.add_cog(Utilities(client))
