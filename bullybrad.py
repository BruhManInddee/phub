import discord
import os
import requests
from bs4 import BeautifulSoup

token = token = os.environ.get('token')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you horny retards :( ~help"))
    
    async def on_message(self, message):
        if message.author.id == "724255896972296222":
            message.delete()
    

client = MyClient()
client.run(token)
