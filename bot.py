import discord
import os
import requests
from bs4 import BeautifulSoup

token = os.environ.get('token')
url = "https://www.pornhub.com/model/"

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you horny retards :( ~help"))

    
    async def on_message(self, message):
        # don't respond to ourselves
        if not message.content.startswith("~"):
            return
        if message.author == self.user:
            return
	
        if not message.channel.nsfw:
            await message.author.send("Put that shit in a nsfw channel bruh")
            return
        
        message.content=message.content[1:len(message.content)].lower()
        args = message.content.split(" ")

	if args[0] == "help":
            embedVar = discord.Embed(title="Commands", color=0xffffff)
            embedVar.add_field(name="NSFW", value="```r34 [tag] \nmodel [phub model]```", inline=False)
            await message.channel.send(embed=embedVar)
	
        if args[0] == 'model':
            url = "https://www.pornhub.com/model/"+args[1]+"/videos"
            await message.channel.send(url)
        #####################################################################
        if args[0] == "r34":
            num=0
            url = "https://rule34.xxx/index.php?page=post&s=list&tags="+args[1]
            response = requests.get(url)
            html = response.text

            soup = BeautifulSoup(html, "html.parser")
            links = soup.findAll("a")
            for link in links:
                if link.get("id"):
                    href = str(link.get("href"))
                    print(href)
                    url = "https://rule34.xxx/"+href
                    response = requests.get(url)
                    html = response.text
                    soup = BeautifulSoup(html, "html.parser")
                    links = soup.findAll("img")
                    for link in links:
                         if str(link.get("id")) == "image":
                                src = str(link.get("src"))
                                if src.startswith("https://"):
                                    num+=1
                                    print(num)
                                    await message.channel.send(src)
                                    if num==6:
                                        msg = await message.channel.send("first 6 r34 results for "+args[1])
                                        await msg.add_reaction("➕")
                                        return
    @staticmethod
    async def on_reaction_add(reaction, user):
        emoji = reaction.emoji
        message = reaction.message
        if user.bot:
            return

        if message.author != client.user:
            
            return

        if emoji == "➕":
            print("go")
            fromnunm = int(message.content.split(" ")[1])
            print(fromnunm)
            num = 0
            url = "https://rule34.xxx/index.php?page=post&s=list&tags="+message.content.split(" ")[5]
            response = requests.get(url)
            html = response.text

            soup = BeautifulSoup(html, "html.parser")
            links = soup.findAll("img")
            for link in links[fromnunm:]:
                href = str(link.parent.get("href"))
                print(href)
                url = "https://rule34.xxx/"+href
                response = requests.get(url)
                html = response.text
                soup = BeautifulSoup(html, "html.parser")
                links = soup.findAll("img")
                for link in links:
                    print("WOOOO")
                    if str(link.get("id")) == "image":
                            src = str(link.get("src"))
                            if src.startswith("https://"):
                                num+=1
                                print(num)
                                await message.channel.send(src)
                                if num==6:
                                    msg = await message.channel.send("next "+str(fromnunm+6)+" r34 results for "+message.content.split(" ")[5])
                                    await msg.add_reaction("➕")
                                    return
        else:
            return

    

client = MyClient()
client.run(token)
