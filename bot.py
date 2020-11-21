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
        if not message.content.startswith("~"):
            return
        if message.author == self.user:
            return

        args = message.content.split(" ")

        if args[0]  == "s":
            await client.delete_message(message)
            result = ' '.join(str(i) for i in args[1:len(args)]) 
            await message.channel.send(result)

client = MyClient()            
client.run(token)
