import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio

# Load environment variables
load_dotenv()

# Set up the bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

@bot.command()
async def load( ctx, extension ):
    bot.load_extension( f'cmds.{extension}' )
    await ctx.send( f'{extension} loaded successfully!')

@bot.command()
async def unload( ctx, extension ):
    bot.unload_extension( f'cmds.{extension}' )
    await ctx.send( f'{extension} unloaded successfully!')

@bot.command()
async def reload( ctx, extension ):
    bot.reload_extension( f'cmds.{extension}' )
    await ctx.send( f'{extension} reloaded successfully!')

async def _load():
    for filename in os.listdir( './cmds' ):
        if filename.endswith( '.py' ):
            try:
                await bot.load_extension(f"cmds.{filename[:-3]}")
            except Exception as e:
                print(f"Failed to load extension {filename}: {e}")

# Run the bot
async def main():
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        raise ValueError("No token found. Make sure DISCORD_TOKEN is set in your environment variables.")
    await _load()
    await bot.start(token)

asyncio.run( main() )