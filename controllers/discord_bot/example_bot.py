import discord

from dotenv import load_dotenv
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

load_dotenv(dotenv_path="../../data/hidden.env")
token = os.getenv('DISCORD_BOT_TOKEN')

client.run(token)