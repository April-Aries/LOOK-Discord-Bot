import discord
from discord.ext import commands
from core.classes import CogExtension
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Event( CogExtension ):

    """
    @commands.Cog.listener()
    async def on_member_join( self, member ):
        channel = self.bot.get_channel( int( os.getenv('WELCOME_CHANNEL') ) )
        await channel.send( f"{member} join!" )

    @commands.Cog.listener()
    async def on_member_remove( self, member ):
        channel = self.bot.get_channel( int( os.getenv('WELCOME_CHANNEL') ) )
        await channel.send( f"{member} leave!" )
    
    @commands.Cog.listener()
    async def on_message( self, msg ):
        if msg.author == self.bot.user: # avoid recursive call
            return
        if msg.content == 'Happy New Year':
            await msg.channel.send( 'Happy New Year!' )
    """

async def setup( bot ):
    await bot.add_cog( Event( bot ) )