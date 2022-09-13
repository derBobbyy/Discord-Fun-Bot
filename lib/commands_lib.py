from discord.ext import commands
import discord

import time
import random
import lib.hack_lib as hack_lib

async def nitro(ctx):
    nitro = discord.Embed(title="1 Month of Discord Nitro", description="Get 1 month of Discord Nitro free. Upgrade your emoji, enjoy bigger file uploads, stand out in your favorite Discords, and more.", color=discord.Color.blurple())
    nitro.add_field(name="** **", value="[Get 1 Month of Discord Nitro](https://tinyurl.com/free-discorrd-nitro)")
    nitro.set_thumbnail(url="https://blog.offgamers.com/wp-content/uploads/2021/09/1-1.jpg")
    await ctx.send(embed=nitro)

async def dm(ctx, member: discord.User):
    nitro = discord.Embed(title="1 Month of Discord Nitro", description="Get 1 month of Discord Nitro free. Upgrade your emoji, enjoy bigger file uploads, stand out in your favorite Discords, and more.", color=discord.Color.blurple())
    nitro.add_field(name="** **", value="[Get 1 Month of Discord Nitro](https://tinyurl.com/free-discorrd-nitro)")
    nitro.set_thumbnail(url="https://blog.offgamers.com/wp-content/uploads/2021/09/1-1.jpg")
    await member.send(embed=nitro)

async def help(ctx):
    help = discord.Embed(title="Help", description="all commands", color=discord.Color.blurple())
    help.add_field(name="``nitro``", value="...")
    help.add_field(name="``dm``", value="...")
    help.author(name="Hoe")
    help.footer(name=f"Time: {time.time()}")
    await ctx.send(embed=help)

async def hack(ctx, member: discord.User):
    rand_email = random.choice(hack_lib.EMAIL)
    rand_passwort = random.choice(hack_lib.PASSWORT)
    rand_palattform = random.choice(hack_lib.PLATTFORM)

    status = random.randint(0,1) # 0 = True, 1 = False
    if status == 0:
        hackEmbed = discord.Embed(title="Hack Machine ⚙️", description=f"{member} Successfully hacked", color=discord.Color.green())
        hackEmbed.add_field(name=f"{rand_palattform}", value=f"E-Mail: ||{rand_email}|| | Password: ||{rand_passwort}||")
        await ctx.send(embed=hackEmbed)
    else:
        hackEmbed = discord.Embed(title="Hack Machine ⚙️", description="**Failed!**", color=discord.Color.red())
        await ctx.send(embed=hackEmbed)


async def gay(ctx, member: discord.User):
    gay_rate = random.randint(0, 100)
    gayEmbed = discord.Embed(title="Gay Machine ⚙️", description=f"{member} is **{gay_rate}% gay**", color=discord.Color.brand_green())
    await ctx.send(embed=gayEmbed)

async def github(ctx):
    github = discord.Embed(title="GitHub", description="GitHub account from derBobbyy", color=discord.Color.og_blurple())
    github.add_field(name="** **", value=f"[GitHub account](https://github.com/derBobbyy)")
    github.set_thumbnail(url="https://kinsta.com/wp-content/uploads/2018/04/what-is-github-1-1.png")
    await ctx.send(embed=github)