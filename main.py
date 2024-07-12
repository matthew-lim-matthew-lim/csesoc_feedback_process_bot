import discord
import os
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()

# Define the intents
intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent

# Our connection to discord with the defined intents
client = discord.Client(intents=intents)

# Use @client.event to register an event.
# Since discord.py is async, we use callback functions (functions that are called when something else happens)
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# Triggers each time a message is received
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv('DISCORD_TOKEN'))
