import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler

load_dotenv()

# Define intents
intents = discord.Intents.default()
intents.message_content = True  # Let the bot do message stuff
intents.guilds = True  # Let the bot access guild information

# Connection to discord with defined intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Schedule pings
scheduler = AsyncIOScheduler()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    print('Connected guilds:')
    for guild in bot.guilds:
        print(f'{guild.name} (ID: {guild.id})')
    scheduler.start()

# Command to manually send the ping
@bot.command()
async def manualping(ctx):
    await send_daily_ping()

# Scheduled task to send a daily ping
async def send_daily_ping():
    guild_id = int(os.getenv('GUILD_ID'))
    channel_id = int(os.getenv('CHANNEL_ID'))

    print(f'Trying to access Guild ID: {guild_id}')
    print(f'Trying to access Channel ID: {channel_id}')

    # Print all guilds the bot is connected to for verification
    print('Connected guilds:')
    for guild in bot.guilds:
        print(f'{guild.name} (ID: {guild.id})')

    guild = bot.get_guild(guild_id)
    if guild:
        try:
            channel = await bot.fetch_channel(channel_id)
            if channel:
                role = discord.utils.get(guild.roles, name="Outreach")
                if role:
                    await channel.send(f'Hello {role.mention}!')
                else:
                    await channel.send('Role "Outreach" not found.')
            else:
                print(f'Channel with ID {channel_id} not found.')
        except discord.NotFound:
            print(f'Channel with ID {channel_id} not found.')
        except discord.Forbidden:
            print(f'Permission denied to access Channel ID {channel_id}.')
        except discord.HTTPException as e:
            print(f'Fetching channel failed: {e}')
    else:
        print(f'Guild with ID {guild_id} not found.')

# Schedule the task to run every day at a specific time (in 24 hour time)
scheduler.add_job(send_daily_ping, 'cron', hour=1, minute=32)

bot.run(os.getenv('DISCORD_TOKEN'))
