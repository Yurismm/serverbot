import discord
from discord.ext import commands

class moderation:
    '''
    Moderation commands
    '''
     
     
def __init__(self, bot):
         self.bot = bot

@commands.command(pass_context = True)
async def ban(member: discord.Member, days: int = 1):
    if "449706643710541824" in [role.id for role in message.author.roles]:
        await bot.ban(member, days)
    else:
        await bot.say("You don't have permission to use this command.")