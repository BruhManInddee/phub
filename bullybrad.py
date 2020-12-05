import discord
import os
import requests
from bs4 import BeautifulSoup

token = token = os.environ.get('token')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="your mum's booty hole"))
    
    args = message.content.split(" ")
    if args[0].lower() != "beeb":
        return
    
    async def on_message(self, message):
        if args[1].lower() == "massnick":
            await message.channel.send("shart")
    

client = MyClient()
client.run(token)
