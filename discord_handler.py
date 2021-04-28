import os
from function import *
import discord
from discord.ext import commands

dcbot = discord.ext.commands.Bot(command_prefix="%")


@dcbot.command()
async def ping(ctx):
    await ctx.send(dcbot.latency)

@dcbot.command()
async def due(ctx):
    data = grab_data()
    for i in data:
        embed = discord.Embed(title=i['name'],
                              url=i['editurl'],
                              description=i['description'], color=0x00ff59)
        embed.set_author(name=i['course']['fullname'],
                         url=i['course']['viewurl'])
        embed.add_field(name="Due date", value=i['timesort'], inline=True)
        embed.add_field(name="Time remaining", value=i['timesort'], inline=True)
        await ctx.send(embed=embed)
