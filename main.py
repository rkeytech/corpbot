import discord
from discord.ext import commands
import os

# Set Intents for the bot
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)

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
    print(f"{bot.user.name} is ready!")
    
@bot.event
async def on_member_join(member):
    print(f"{member} joined the server!")

# -------------------------------
# Commands


# # -----------------------------
bot.run(os.getenv('TOKEN'))