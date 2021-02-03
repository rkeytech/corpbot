import discord
from discord.ext import commands


class Pilot(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.restricted_roles = ['CEO', 'Directors']

    # Events
    # Create events with @commands.Cog.listener()

    # Commands
    # Create commands with @commands.command()
    @commands.command()
    async def ign(self, ctx, *, nick=None):
        member = ctx.message.author
        guild = self.client.guilds[0]
        try:
            nick = nick
            if nick:
                pilot = discord.utils.get(guild.roles, name='Pilots')
                await member.edit(nick=nick)
                await member.add_roles(pilot)
        except Exception as e:
            print(e.args[0])

    @commands.command()
    async def career(self, ctx, career=None):
        guild = self.client.guilds[0]
        member = ctx.message.author
        member_roles = [role.name for role in member.roles]
        if 'Pilots' in member_roles:
            career = f"{career.lower().capitalize()}s"
            try:
                if career not in self.restricted_roles:
                    role = discord.utils.get(guild.roles, name=career)
                    await member.add_roles(role)
                else:
                    await ctx.message.channel.send(
                        f"{member.nick.capitalize()} the career of {career} \
                            you are trying to focus is not for you! For now \
                            at least. Try another one!"
                    )
            except Exception as e:
                print(e.args[0])
        else:
            await ctx.message.channel.send(
                f'{member.nick} please use first the command `!ign` to set \
                    your in game nickname and become a pilot \
                    of our corporation!'
            )


def setup(client):
    client.add_cog(Pilot(client))
