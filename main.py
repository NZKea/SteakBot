import random
import discord
from discord.ext import tasks, commands
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
steakBot = commands.Bot(command_prefix='$SteakBot ', intents=intents)


async def switch_status(name):
    await steakBot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching,name=name))


@steakBot.event
async def on_ready():
    print("Systems Online")

replies = ["🤖 ✅ ", "🥩", "🐄", "https://media.giphy.com/media/RLJrfLPa5jD2FoWrOO/giphy.gif", "https://media.giphy.com/media/unQ3IJU2RG7DO/giphy.gif", "https://tenor.com/view/rare-rare-steak-steak-cutting-steak-gif-11709098"]

@steakBot.command(name="reload")
async def reload_status(ctx):
    steakBot.reload_extension("cogs.statusCog")
    print("Reload")
    await ctx.reply(random.choice(replies), mention_author=True)


steakBot.load_extension("cogs.statusCog")
steakBot.run(TOKEN)