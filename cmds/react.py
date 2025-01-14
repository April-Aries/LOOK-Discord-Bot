import discord
from discord.ext import commands
from core.classes import CogExtension
import datetime
import random
import json

class React( CogExtension ):

    @commands.command()
    async def chooseDinner(self, ctx):
        try:
            with open("dinner.txt", "r") as file:
                dinners = [line.strip() for line in file if line.strip()]
                file.close()
        except (FileNotFoundError, json.JSONDecodeError):
            dinners = []

        choice = random.choice(dinners)
        await ctx.send( f"{ctx.author.display_name} 晚安！我覺得 **{choice}** 或許是個不錯的選擇！" )

    @commands.command()
    async def listDinner(self, ctx):
        try:
            with open("dinner.txt", "r") as file:
                dinners = [line.strip() for line in file if line.strip()]
                file.close()
        except (FileNotFoundError, json.JSONDecodeError):
            dinners = []
        
        reply = "目前晚餐選項有："
        for dinner in dinners:
            reply += f"{dinner}、"
        reply = reply[:-1]
        await ctx.send(reply)
    
    @commands.command()
    async def addDinner(self, ctx, *, newDinner: str):
        try:
            with open("dinner.txt", "r") as file:
                dinners = [line.strip() for line in file if line.strip()]
                file.close()
        except (FileNotFoundError, json.JSONDecodeError):
            dinners = []

        if newDinner in dinners:
            await ctx.send(f"{newDinner} 已經在晚餐清單裡面囉！")
        else:
            dinners.append(newDinner)

            with open("dinner.txt", "w") as file:
                file.write("\n".join(dinners))
                file.close()

            await ctx.send(f"已新增 **{newDinner}** 到晚餐清單")

    @commands.command()
    async def removeDinner(self, ctx, *, wanted: str):
        try:
            with open("dinner.txt", "r") as file:
                dinners = [line.strip() for line in file if line.strip()]
                file.close()
        except (FileNotFoundError, json.JSONDecodeError):
            dinners = []

        if wanted not in dinners:
            await ctx.send(f"{wanted} 不在晚餐清單裡面耶！")
        else:
            dinners.remove(wanted)

            with open("dinner.txt", "w") as file:
                file.write("\n".join(dinners))
                file.close()

            await ctx.send(f"已從晚餐清單移除 **{wanted}**")

async def setup( bot ):
    await bot.add_cog( React( bot ) )