import discord
from discord.ext import commands
from core.classes import CogExtension
import asyncio, datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Task(CogExtension):
    def __init__(self, bot):
        self.bot = bot
        self.bg_task = None  # Initialize bg_task to None
        self.counter = 0
    
    async def interval(self):
        await self.bot.wait_until_ready()
        self.channel = self.bot.get_channel(os.getenv('TEST_CHANNEL'))
        while not self.bot.is_closed():
            await self.channel.send('Hi! LOOK is running')
            await asyncio.sleep(1)
    
    @commands.Cog.listener()
    async def on_ready(self):  # Use on_ready event to start the background task
        self.bg_task = self.bot.loop.create_task(self.time_task())
        #self.bg_task = self.bot.loop.create_task(self.interval())

async def setup(bot):
    await bot.add_cog(Task(bot))
