import discord
import asyncio
import ruamel.yaml as yaml

with open('config.yml', 'r') as config_file:
    try:
        cfg = yaml.safe_load(config_file)
    except yaml.YAMLError as exc:
        print(exc)

class Client(discord.Client):
    async def on_ready(self):
        print('Ready!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('!ping'):
            await message.channel.send('Pong!')

client = Client()
client.run(cfg['discord']['token'])
