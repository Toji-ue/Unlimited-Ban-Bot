import os 
import random
import json
import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import MissingPermissions


intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

def load_banned_games():
    if not os.path.exists("banned_games.json"):
        with open("banned_games.json", "w") as f:
            json.dump(["League of Legends"], f)
    with open("banned_games.json", "r") as f:
        banned_games = json.load(f)
        if not banned_games:
            banned_games.append("League of Legends")
            with open("banned_games.json", "w") as f:
                json.dump(banned_games, f)
        return banned_games

def save_banned_games(banned_games):
    with open("banned_games.json", "w") as f:
        json.dump(banned_games, f)

with open("banned_games.json", "r") as f:
    banned_games = json.load(f)
banned_games = load_banned_games()
random_activity = ["Making the world better",
                   f"Imagine playing {random.choice(banned_games)}",
                   "Please Live Healthy",
                   "Always Grinding",
                   "Decrease World Obesity [-------10%]"]
message = ["Please Take a Shower",
           "Havent touch Grass yet?",
           "Go get a life, Stop playing",
           "Hit the gym Homie",
           "stop playing and you will find some bitches"]
@bot.event
async def on_ready():
    print(r"""\⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⠤⡤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣶⠞⠋⢡⠀⠀⠀⢠⡀⠀⠉⠙⠲⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⢞⣉⡴⢁⡾⠁⠀⠀⢸⡆⠀⠀⠀⠉⠳⣦⡀⠀⠈⠋⠳⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡴⢟⡿⠋⠈⠀⣼⠁⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠙⢶⣄⠀⠀⠀⠙⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⠟⢄⡞⠀⠀⠀⢨⡏⠀⠀⠀⠀⠀⠈⢷⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠂⠈⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⠿⢀⡞⠀⠀⠀⠀⢻⡇⠀⠀⠀⣀⣀⢀⡈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠳⡄⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⠟⠀⣾⠀⠀⠀⠐⠲⣼⡇⢀⠀⣾⡏⢹⣷⡀⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠹⡆⠀⠀⠀⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣾⠀⢸⠇⠀⢀⣀⣀⣠⠿⠿⠾⠷⢾⡇⢸⡟⠋⠛⠋⠉⠉⠙⠓⠒⠲⠶⠦⣼⢽⡄⠀⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣼⠋⠀⣿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠠⢿⡀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣿⠀⢠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠈⡷⢄⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀
⠀⢸⠁⠸⢹⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣶⠀⢹⡀⠀⠈⣿⠀⠀⠀⠀⠀⠀⠀
⠀⣼⠀⠀⣿⣽⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⣿⢦⡜⢷⠄⠀⣿⡄⠀⠀⠀⠀⠀⠀
⢀⡏⠀⠀⣿⢺⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡿⠀⠀⠀⠀⠀⢻⡇⠀⠀⠀⠀⠀⠀
⢸⡇⠀⠀⣿⢼⡇⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀
⣾⣿⠀⡀⢹⣼⡇⠀⠀⠀⠀⠀⣿⣿⠆⠀⠀⠐⠒⠒⠒⠀⠀⢼⣿⡷⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀
⣿⣿⣄⢣⠸⣿⡇⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⡇⠀⠈⢳⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀  Made by Toji With Love ♡
⣿⡇⣏⡄⣧⢺⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢸⠀⠀⣸⡇⠀⠀⠀⠀⠀⠀Ready To Purge Overweight People 
⣿⣿⣿⡃⠈⠈⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢰⠀⢸⠀⠀⣾⡇⠀⠀⠀⠀⠀⠀
⢹⣧⢻⡆⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢸⠀⢸⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀
⢸⣿⢸⡇⢠⣀⠻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⡿⠀⢸⠀⠀⢺⣷⠀⠀⠀⠀⠀⠀
⠈⣿⣆⡇⠀⢹⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⡇⠀⢸⠀⠀⢸⢸⠀⠀⠀⠀⠀⠀
⠀⠸⣿⣧⠀⣾⡟⡷⢤⣤⣤⠴⣶⣶⣶⠶⣶⣶⣖⣲⠒⢒⣒⣶⣶⣷⣾⠒⣶⢲⠒⠲⣿⠇⠀⢸⠀⠄⣾⢸⠀⠀⠀⠀⠀⠀
⠀⠀⠹⣿⡄⢸⡇⢹⡄⠀⢹⠀⢸⡀⢾⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡿⢻⠀⣿⢸⡄⠀⡞⠀⠀⢸⢀⡄⣿⢺⡆⠀⠀⠀⠀⠀
⠀⠀⠀⠙⣿⠀⡇⠐⣇⠀⢸⠀⠈⣇⢸⣇⣬⣿⣿⣹⣿⣿⣿⣿⠟⠀⢸⣤⣏⢸⠆⢠⡇⠀⠀⢸⠀⠁⢯⢸⣷⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⡆⣧⠀⠹⡄⠘⡇⠀⣿⣿⣿⣿⡟⢿⣿⣿⠿⠟⠁⠀⠀⠸⣿⣿⣿⣀⣾⠀⠀⠀⠸⠀⠀⠸⡖⢹⡀⠀⠀⠀⠀
⠀⠀⠀⠀⢻⠀⣿⠀⠀⢧⢠⣧⣼⣿⣿⣿⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢹⣿⢹⣿⣶⣶⣤⣀⡀⠀⠀⢻⠘⡇⠀⠀⠀⠀
⠀⠀⠀⠀⢸⠀⣹⣠⣴⣾⣾⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡿⣸⣿⣿⣿⣿⣿⣿⣿⣶⣾⣤⣷⠀⠀⠀⠀
⠀⠀⣀⣠⠾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⢀⣀⣀⣤⣄⣀⠀⠀⣾⣿⣷⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣽⣿⣿⣷⣤⡀
⣴⣿⣿⣿⣷⣶⣤⣤⣌⣙⣛⡻⠿⣿⣿⣿⣿⣿⡟⢛⣋⣉⣁⣈⡛⡿⣾⣿⣿⣿⣿⠟⣋⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
""")
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    print(f'Successfully logged in and booted...!')
    while True:
        game = discord.Game(name=random.choice(random_activity))
        await bot.change_presence(activity=game)
        await asyncio.sleep(5)
@bot.event 
async def on_command_error(ctx, error): 
    if isinstance(error, commands.CommandNotFound): 
        em = discord.Embed(title=f"❌ Error!!!", description=f"Command not found.", color = discord.Colour.random()) 
        await ctx.send(embed=em)
@bot.command()
@commands.has_permissions(ban_members=True)
async def purge(ctx):
    banned = []
    with open("banned_games.json", "r") as f:
      banned_games = json.load(f)
    for i, member in enumerate(ctx.guild.members):
        if member.activity is not None and member.activity.name.lower() in [game.lower() for game in banned_games]:
            await member.send(f"You have been banned from **{ctx.guild.name}** for playing a banned game: " + f"**{member.activity.name}**" + ".")
            await member.send(f"**{random.choice(message)}**")
            await member.ban(reason=f"Playing banned game: **{member.activity.name}**")
            banned.append(member)
    if not banned:
        return await ctx.send("No members to ban.")
    embed = discord.Embed(title=f"Banned Members: {len(banned)}", color = discord.Colour.random())
    for i, member in enumerate(banned):
        embed.add_field(name=f"#{i+1} {member.name}", value=member.activity.name, inline=False)
    embed.set_thumbnail(url=ctx.guild.icon.url)
    await ctx.send(embed=embed)
@purge.error
async def purge_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send(f"User **{ctx.author.name}** has no permissions. Requires permissions: **Ban Members**")
@bot.command()
@commands.has_permissions(ban_members=True)
async def kick(ctx):
    kicked = []
    with open("banned_games.json", "r") as f:
      banned_games = json.load(f)
    for i, member in enumerate(ctx.guild.members):
        if member.activity is not None and member.activity.name.lower() in [game.lower() for game in banned_games]:
            await member.send(f"You have been banned from **{ctx.guild.name}** for playing a banned game: " + f"**{member.activity.name}**" + ".")
            await member.send(f"**{random.choice(message)}**")
            await member.kick(reason=f"Playing banned game: **{member.activity.name}**")
            kicked.append(member)
    if not kicked:
        return await ctx.send("No members to ban.")
    embed = discord.Embed(title=f"Kicked Members: {len(kicked)}", color = discord.Colour.random())
    for i, member in enumerate(kicked):
        embed.add_field(name=f"{i+1}. {member.name}", value=member.activity.name, inline=False)
    embed.set_thumbnail(url=ctx.guild.icon.url)
    await ctx.send(embed=embed)
@kick.error
async def purge_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send(f"User **{ctx.author.name}** has no permissions. Requires permissions: **Ban Members**")
@bot.command()
@commands.has_permissions(administrator=True)
async def gban(ctx, *, game_name: str):
    banned_games = load_banned_games()
    if game_name in banned_games:
        await ctx.send(f'**{game_name}** is already banned.')
        return
    banned_games.append(game_name)
    save_banned_games(banned_games)
    await ctx.send(f'Successfully banned game: **{game_name}**')
@gban.error
async def purge_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send(f"User **{ctx.author.name}** has no permissions. Requires permissions: **Admin**")
@bot.command()
@commands.has_permissions(administrator=True)
async def gunban(ctx, *, game_name: str):
    if game_name in banned_games:
        banned_games.remove(game_name)
        save_banned_games(banned_games)
        await ctx.send(f'Successfully unbanned game: **{game_name}**')
    else:
        await ctx.send(f'Game **{game_name}** is not banned.')
@gunban.error
async def purge_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send(f"User **{ctx.author.name}** has no permissions. Requires permissions: **Admin**")
@bot.command()
async def banlist(ctx):
    with open("banned_games.json", "r") as f:
      banned_games = json.load(f)
    if not banned_games:
        await ctx.send("No banned games.")
    else:
        embed = discord.Embed(title=f"Banned Games in **{ctx.guild.name}**", color=0x00ff00)
        for i, game in enumerate(banned_games):
            embed.set_thumbnail(url=ctx.guild.icon.url)
            embed.add_field(name=f"{i + 1}.", value=game, inline=False)
        await ctx.send(embed=embed)
@bot.command()
async def help(ctx):
    await ctx.send("Im lazy asf to make this")
    await ctx.send("so this is a list of commands")
    await ctx.send("purge (ban member), kick (kick member), gban(banning game), gunban (unban game), banlist (a list of banned games)")
bot.run('YOUR_TOKEN')