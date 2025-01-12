import discord
from discord.ext import commands
from core.classes import CogExtension
import datetime
import random

class React( CogExtension ):

    @commands.command()
    async def hi( self, ctx ):
        await ctx.send( "Hi there!" )

    @commands.command()
    async def dinner(self, ctx):
        await ctx.send( f"Good evening, {ctx.author.display_name}" )
        dinnerList = [
            "義大利麵", "披薩", "便當", "臭豆腐", "滷肉飯", "蔥油餅", "蚵仔煎", "牛肉麵", "割包", "小籠包", "水餃", "蛋餅"
        ]
        choice = random.choice(dinnerList)
        await ctx.send( f"我覺得 **{choice}** 或許是個不錯的選擇！" )

async def setup( bot ):
    await bot.add_cog( React( bot ) )