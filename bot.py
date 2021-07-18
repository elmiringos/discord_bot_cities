import discord
import os
from discord.ext import commands

client = commands.Bot( command_prefix = '.')

hello_words = ['hello', 'hi', 'privet', 'привет']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command( pass_context = True)


@client.event

async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'здарова, {author.mention}!')
""" async def on_message(message):
    author = message.author
    msg = message.content.lower()
    await client.process_commands( message )

    if msg in hello_words:
    	await message.channel.send('Привет') """



    



client.run(os.environ['DISCORD_BOT_TOKEN'])