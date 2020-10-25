import os
import discord
from discord.ext import commands

token = os.environ.get('token')
bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)
print("on")
print(token)
