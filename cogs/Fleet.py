import discord
from discord.ext import commands


class Fleet(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    # Create events with @commands.Cog.listener()

    # Commands
    # Create commands with @commands.command()
    @commands.command()
    async def fleetup(self, ctx, tm=60, place='our station'):
        member = ctx.message.author
        guild = self.client.guilds[0]
        cat = discord.utils.get(guild.categories, name='Fleets')
        if member.top_role.name == 'Directors':
            try:
                dir_role = member.roles[-2]
            except Exception:
                dir_role = 'General'
            fleet_name = f"{dir_role.name} fleet"
            fleet_channel = await guild.create_text_channel(
                name=fleet_name, category=cat
            )
            mbed = discord.Embed(
                title=f"Fleet up for {fleet_name.split(' ')[0].capitalize()}",
                colour=member.roles[-2].color
            )
            mbed.add_field(
                name='__Take Action__',
                value=f"React to this message, with any reaction, if your are \
                    interested in participating in the \
                    {fleet_name.split(' ')[0].capitalize()} Operation taking \
                    place in **{tm} minutes** at **{place}**."
            )
            mbed.set_author(name=member.nick, icon_url=member.avatar_url)
            msg = await fleet_channel.send(embed=mbed)
            await msg.pin()
        else:
            await ctx.message.channel.send(
                f'{member.nick} only **Directors** can form fleets!'
            )

    @commands.command()
    async def ready(self, ctx):
        member = ctx.message.author
        guild = self.client.guilds[0]
        pilots = set()
        if member.top_role.name == 'Directors':
            if ctx.message.channel.category.name == 'Fleets':
                v_channel = await guild.create_voice_channel(
                    name=ctx.message.channel.name,
                    category=guild.get_channel(804891415942660110).category
                )
                pinned = await ctx.message.channel.pins()
                msg = await ctx.message.channel.fetch_message(pinned[0].id)
                for reaction in msg.reactions:
                    users = await reaction.users().flatten()
                    pilots.update(users)
                for pilot in pilots:
                    await pilot.move_to(v_channel)
                await ctx.message.channel.purge(bulk=False)
            else:
                await ctx.message.channel.send(
                    f'{member.nick} you must be in a Fleet Channel to make the \
                        appropriate fleet ready for action!'
                )

        else:
            await ctx.message.channel.send(
                f'{member.nick} only **Directors** can make \
                    the fleet ready for action!')


def setup(client):
    client.add_cog(Fleet(client))
