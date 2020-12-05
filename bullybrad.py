import discord
import os
import requests
from bs4 import BeautifulSoup

token = os.environ.get('token')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Fuck off </3"))
    
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        args = message.content.split(" ")
        if args[0].lower() != "beeb":
            return
                                                               
        if args[1].lower() == "massnick":
            await message.channel.send("shart")
    

client = MyClient()
client.run(token)
