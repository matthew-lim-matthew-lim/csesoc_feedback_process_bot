import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import json

load_dotenv()

# Define intents
intents = discord.Intents.default()
intents.message_content = True  # Let the bot do message stuff
intents.guilds = True  # Let the bot access guild information

# Connection to discord with defined intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Schedule pings
scheduler = AsyncIOScheduler()

DATA_FILE = "jira_data.json"

def read_data_for_bot():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def clear_file(file_path):
    with open(file_path, 'w') as file:
        # Opening in 'w' mode clears the file
        pass

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
        channel = await bot.fetch_channel(channel_id)
        data = read_data_for_bot()
        for issue_summary, issue_data in data.items():
            issue_url = issue_data.get('issue_url')
            responsible_ports = issue_data.get('issue_responsible_ports')
            if issue_url and responsible_ports:
                message = f"Hello! An even needs feedback to be collected: {issue_summary}.\n"
                message += f"Please check the the JIRA ticket at: {issue_url}\n"
                message += f"Responsible ports:\n"
                for port in responsible_ports:
                    member = discord.utils.get(guild.roles, name=port)
                    message += f"{member.mention}\n"

                await channel.send(message)
            else:
                print(f"Missing data for issue: {issue_summary}")
        clear_file(DATA_FILE)
    else:
        print(f'Guild with ID {guild_id} not found.')

# Schedule the task to run every day at a specific time (in 24 hour time)
scheduler.add_job(send_daily_ping, 'cron', hour=1, minute=32)

bot.run(os.getenv('DISCORD_TOKEN'))
