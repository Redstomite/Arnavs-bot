import discord.member
from discord.ext import commands
from discord.ext.commands import has_permissions
import os.path

tolkein = os.getenv('DISCORD_BOT_TOKEN')
TOKEN = "Nzg0MDIwOTgwNDU5NzY1NzYy.X8jOcA.dYethgEOhssN7b6Wl-oah32MOzw"
bot = commands.Bot(command_prefix='}')


@bot.event
async def on_ready():
    print("up and running")
    await bot.change_presence(activity=discord.Game(name="dev - EY_Sviper#4342 || }help"))


@bot.command(name='info')
async def info(ctx):
    response = "Bot developed by EY_Sviper#4342 for '1 invite an nfa mc acc'. '}' is the prefix. Contact EY_Sviper#4342" \
               "for any queries, bug reports, questions, or custom bots for your server :)"
    await ctx.send(response)


@bot.command(name='lock')
@has_permissions(manage_channels=True)
async def lock(ctx, name: str):
    channel = discord.utils.get(ctx.guild.channels, name=name)
    overwrite = channel.overwrites_for(ctx.message.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    response = 'Channel locked by '+ str(ctx.message.author)
    await channel.send(response)


@bot.command(name='unlock')
@has_permissions(manage_channels=True)
async def lock(ctx, name:str):
    print(name)
    channel = discord.utils.get(ctx.guild.channels, name=name)
    overwrite = channel.overwrites_for(ctx.message.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    response = 'Channel unlocked by '+ str(ctx.message.author)
    await channel.send(response)

bot.run(TOKEN)
