import os
import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

url = "https://www.pornhub.com"

token = os.environ.get('token')
bot = commands.Bot(command_prefix='~')

@bot.command()
async def vid(ctx):
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    links = soup.findAll("a")
    for link in links:
        href = str(link.get("href"))
        if href.startswith("/view") and href[-1].isdigit():
            response = requests.get("https://pornhub.com"+href)
            html = response.text
            soup = BeautifulSoup(html, "html.parser")
            links = soup.findAll('title')
            sentence = str(link)[7:len(link)-9]+" - https://pornhub.com"+str(href)
            await ctx.send(sentence)

bot.run(token)
print("on")
print(token)
