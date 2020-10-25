import discord
import os

token = os.environ.get('token')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
        	return
	
	if not message.content.startswith("~"):
		return
	
	message.content = message.content[1:len(message.content)].lower()

        if message.content == 'ping':
        	await message.channel.send(message.content)

client = MyClient()
client.run(token)
