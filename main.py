import discord
import sys
from discord.ext import commands
import pypi

intents = discord.Intents().all()
intents.message_content = True
bot = commands.Bot(command_prefix=('pyp!'), intents=intents)

@bot.event
async def on_ready():
    activity = discord.Activity(name='ライブラリ', type=discord.ActivityType.watching)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print('OK!')

@bot.command()
@commands.cooldown(1, 10, type=commands.BucketType.user)
async def search(ctx, word: str):
    await ctx.reply(embed=discord.Embed(title=f"PyPi検索 - {word}", description=f"{await pypi.pypititle(word, 0)} ->\n{await pypi.pypiurl(word, 0)}"))
    
bot.run("tokenを入れる")
