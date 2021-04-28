import os
from function import *
import discord
from discord.ext import commands
import html
from datetime import datetime
from datetime import timedelta
from datetime import timezone
import pytz

dcbot = discord.ext.commands.Bot(command_prefix="%")

@dcbot.command()
async def ping(ctx):
    await ctx.send(dcbot.latency)

@dcbot.command()
async def due(ctx):
    await ctx.send(embed=discord.Embed(title="Fetching Data....", color=0x00ff59))
    data = grab_data()
    for i in data:
        embed = discord.Embed(title=i['name'],
                              url=html.unescape(i['action']['url']),
                              description=i['description'], color=0x00ff59)
        embed.set_author(name=i['course']['fullname'],
                         url=i['course']['viewurl'])
        embed.add_field(name="Due date", value=datetime.fromtimestamp(i['timesort'], tz=timezone(timedelta(hours=8))).strftime('%Y-%m-%d %H:%M:%S'), inline=True)
        embed.add_field(name="Days remaining", value=str((datetime.fromtimestamp(i['timesort'], tz=timezone(timedelta(hours=8)))-datetime.now(timezone(timedelta(hours=8)))).days), inline=True)
        await ctx.send(embed=embed)
