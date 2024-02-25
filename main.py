import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="leaver!", intents=discord.Intents.all())

@bot.event
async def on_ready():
  for guild in bot.guilds:
    await guild.leave()

bot.run("TYPE BOT TOKEN")
