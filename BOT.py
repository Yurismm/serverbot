import discord
from discord.ext import commands
import re
import json
import logging
import random
import inspect
import traceback
import os
import aiohttp
import sys
import time

prefix = "+"
bot = commands.Bot(command_prefix=prefix)

extensions = [
    "cogs.math"
]

@bot.event
async def on_ready():
    print("Bot is ready. Spam me owo")

@bot.command()
async def ping(ctx):
    '''Pong! Get the bot's response time'''
    em = discord.Embed(color=discord.Color(value=0x00ff00))
    em.title = "Pong!"
    em.description = f'{bot.ws.latency * 1000:.4f} ms'
    await ctx.send(embed=em)

@bot.command()
async def say(ctx, *, content:str):
    '''Make's assbot say any message you put'''
    await ctx.send(content)

@bot.command()
async def presence(ctx, Type=None, *, thing=None):
    """Change the bots presence"""
    if Type is None:
        await ctx.send(
            'Usage: +presence [game/stream] [msg] OR +presence clear')
    else:
        if Type.lower() == 'stream':
            await bot.change_presence(
                activity=discord.Streaming(
                    name=thing, url='https://www.twitch.tv/monstercat'))
            await ctx.send(f'I am now streaming {thing}!')
        elif Type.lower() == 'game':
            await bot.change_presence(activity=discord.Game(name=thing))
            await ctx.send(f'I am now playing {thing}!')
        elif Type.lower() == 'clear':
            await bot.change_presence(activity=None)
            await ctx.send("Stopped playing/streaming")
        else:
            await ctx.send(
                'Usage: +presence [game/stream] [msg] OR +presence clear')

if __name__ == '__main__':
    for extension in extensions:

        try:
            bot.load_extension(extension)


        except Exception as error:
            print("{} cannot be loaded [{}]".format(extension,error))

    bot.run('NTE4OTEzNDY0OTUwMDYzMTA0.DuXsfA.IEeiRzEgcfwPX1ZIDaEiMgKwOpw')    

