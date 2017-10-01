import discord
import asyncio
import ruamel.yaml as yaml

with open('config.yml', 'r') as config_file:
    try:
        cfg = yaml.safe_load(config_file)
    except yaml.YAMLError as exc:
        print(exc)

client = discord.Client()

@client.event
async def on_ready():
    print('Ready!')

@client.event
async def on_message(message):
    if message.content.startswith('!ping'):
        await client.send_message(message.channel, 'Pong!')

client.run(cfg['discord']['token'])
