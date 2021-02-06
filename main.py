import discord
from discord.ext import commands
import os
import logging


# Configure logging for Bot
logger = logging.getLogger('corpbot')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='corpbot.log', mode='w', encoding='utf-8'
)
handler.setFormatter(
    logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s')
)
logger.addHandler(handler)

# Set Intents for the bot
intents = discord.Intents(messages=True, guilds=True,
                          reactions=True, members=True, presences=True)

bot = commands.Bot(command_prefix='!', intents=intents)

# Load COGS
with os.scandir('./cogs') as it:
    for file in it:
        if file.name.endswith('.py'):
            bot.load_extension(f"cogs.{file.name.split('.')[0]}")

# -------------------------------
# Events

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online!")

@bot.event
async def on_new_member_join():
    chnl = discord.utils.get(bot.guilds[0].text_channels, name='welcome-aboard')
    mbed = discord.Embed(
        title = 'Commands',
        description = 'A list of commands you have to enter in order to become a pilot of our corporation and have the appropriate permissions in channels.',
        color = discord.Color.magenta()
    )
    mbed.set_author(
        name = bot.name,
        icon_url = bot.avatar_url
    )
    mbed.add_field(
        name = '!ign',
        value = 'A command for setting your in game nickname. It must be the first command so you can procced to choosing your career.',
        inline = True
    )
    mbed.add_field(
        name = '!career',
        value = 'A command for setting your preferred career in our corporation. It gives you the appropriate permissions for specific channels. You can choose between explorer, miner, fighter.',
        inline = True
    )
    mbed.add_field(
        name = '!alt',
        value = 'A command for setting your alternative characters in our corporation. There will be their nick name next to your main character.',
        inline = False
    )
    await chnl.send(embed=mbed)


# -------------------------------
# Commands


# # -----------------------------
bot.run(os.getenv('TOKEN'))
