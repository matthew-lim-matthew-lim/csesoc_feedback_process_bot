import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

# Use !getguild to get the guild id, or !getchannel to get the channel id 

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(pass_context=True)
async def getguild(ctx):
    guild_id = ctx.guild.id
    await ctx.send(f'This server\'s ID is {guild_id}')

@bot.command(pass_context=True)
async def getchannel(ctx):
    channel_id = ctx.channel.id
    await ctx.send(f'This channel\'s ID is {channel_id}')

bot.run(os.getenv('DISCORD_TOKEN'))
