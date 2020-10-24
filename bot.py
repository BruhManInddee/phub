import discord
from boto.s3.connection import S3Connection
s3 = S3Connection(os.environ['S3_KEY'], os.environ['S3_SECRET'])
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('NTU2OTQ2MDQ2Njc3NDE4MDA1.XI62bQ.mizsKEBOeMF-HTrVq_IrIiPO4g4')
