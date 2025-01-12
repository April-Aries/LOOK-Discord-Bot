import discord
from discord.ext import commands
from core.classes import CogExtension

class Main( CogExtension ):

    @commands.command()
    async def ping( self, ctx ):
        await ctx.send( f"{ round( self.bot.latency * 1000 ) } (ms)" )
    
    @commands.command()
    async def say( self, ctx, *, msg ):
        await ctx.message.delete()
        await ctx.send( msg )
    
    @commands.command()
    async def purge( self, ctx, num: int ):
        await ctx.channel.purge( limit = num + 1 )

async def setup( bot ):
    await bot.add_cog( Main( bot ) )