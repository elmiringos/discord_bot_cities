import discord
import os
from discord.ext import commands

client = commands.Bot( command_prefix = '!', intents=discord.Intents.all())

hello_words = ['hello', 'hi', 'privet', 'привет']

cities = ["aa", "bb"]
used_cities = []
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def test(ctx):
    await ctx.send(used_cities)

@client.command()
async def повтор(ctx, *, arg):
    await ctx.send(arg)


@client.command()
async def города(ctx):
    await ctx.send("я готовая")
@client.command()
async def ход(ctx, arg):
    await ctx.send("я запомнил")
    used_cities.append(arg)
    check = False
    for i in cities:
        if i[0] == arg[-1] and i not in used_cities:
            await ctx.send(i)
            used_cities.append(i)
            await ctx.send("твой ход")
            await ctx.send(used_cities)
            check = True
            break
    if check == False:
        await ctx.send("я проиграл ((")
        used_cities = []
        









client.run(os.environ['DISCORD_BOT_TOKEN'])
