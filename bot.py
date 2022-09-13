import discord
from discord.ext import commands

import config
import time
import random
import lib.hack_lib as hack_lib
import lib.commands_lib as commands_lib
import lib.slashcommands_lib as slashcommands_lib

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())

SERVER_IDS = ["889806683449217034"]


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}") 


@bot.command()
async def nitro(ctx): # ?nitro
    await commands_lib.nitro(ctx)

@bot.command()
async def dm(ctx, member: discord.User): #?dm @derBobbyy
    await commands_lib.dm(ctx, member)

@bot.command()
async def list(ctx): # Simple Help command
    await commands_lib.help(ctx)


@bot.command()
async def gay(ctx, member: discord.User): #Simple fun gay command
    await commands_lib.gay(ctx, member)

@bot.command()
async def hack(ctx, member: discord.User): #?hack @derBobbyy | Fun Hack command
    await commands_lib.hack(ctx, member)

@bot.command()
async def github(ctx):
    await commands_lib.github(ctx)



#####     Slash Commands

@bot.slash_command(name="nitro", guild_ids=[SERVER_IDS]) # Nitro slash command
async def nitro(ctx):
    await slashcommands_lib.nitro(ctx)



@bot.slash_command(name="dm", guils_ids=[SERVER_IDS]) # nitro dm slash command
async def dm(ctx, member: discord.User):
    await slashcommands_lib.dm(ctx, member)

    

@bot.slash_command(name="gay", guild_ids=[SERVER_IDS]) # gay machine slash command
async def gay(ctx, member: discord.User):
    await slashcommands_lib.gay(ctx, member)


@bot.slash_command(name="hack", guild_ids=[SERVER_IDS]) # hack slash command
async def hack(ctx, member: discord.User):
    await slashcommands_lib.hack(ctx, member)

@bot.slash_command(name="github", guild_ids=[SERVER_IDS]) # GitHub command
async def github(ctx):
    await slashcommands_lib.github(ctx)


bot.run(config.TOKEN)