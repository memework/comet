import discord
import asyncio
import config
import ruamel.yaml as yaml

with open('config.yml', 'r') as config_file:
    cfg = YAML(typ='safe').load(config_file)

client = discord.Client()

@client.event
async def on_ready():
    print('Ready!')

@client.event
async def on_message(message):
    if message.content.startswith('!ping'):
        tmp = await client.send_message(message.channel, 'Pong!')

client.run(cfg.discord.token)
