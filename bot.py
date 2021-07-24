import discord
import os
from discord.ext import commands


file_citites = open("cities.txt")
all_cities = [file_citites.readline().strip() for i in range(323)]
file_citites_for_bot = open("cities_for_bot.txt")
cities_for_bot = [file_citites_for_bot.readline().strip().lower() for i in range(48)]
print(cities_for_bot)
client = commands.Bot( command_prefix = '!', intents=discord.Intents.all())
hello_words = ['hello', 'hi', 'privet', 'привет']
used_cities = []
LETTERS_TO_SKIP = ["ь", "ъ", "ы"]
steps = []
BOT_NAME = "Amirjanus#2306"

async def user_step(ctx, city):
    if city not in all_cities:
        await ctx.send("Такого города не существует")
        return 

    if len(used_cities) != 0:
        letter_for_step = last_letter(used_cities[-1])  

    if city in used_cities:
        await ctx.send("ошибка 1.Такой город уже был, напишите другой город")
        return

    if len(used_cities) != 0 and letter_for_step != city[0].lower():
        await ctx.send("ошибка 2. Вы должны назвать город на букву {0}".format(letter_for_step))
        return

    used_cities.append(city)
    
def city_for_bot():
    print(used_cities)
    letter_for_step = last_letter(used_cities[-1])
    print(letter_for_step)
    for i in cities_for_bot:
        print(used_cities)
        print(letter_for_step)
        print(i)
        if i[0] == letter_for_step and i not in used_cities:
            return i

async def bot_step(ctx):
    if ctx.author == BOT_NAME:
        return

    if len(used_cities) == 0:
        return
    city = city_for_bot()
    if city:
        used_cities.append(city)
        await ctx.send(city)
        await ctx.send("Твой ход")
    else:
        await ctx.send("Я проиграл")

def last_letter(city):
    if city[-1] in LETTERS_TO_SKIP:
        return city[-2]
    else: 
        return city[-1]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def inf(ctx):
    await ctx.send("!города\n", "!ход\n")

@client.command()
async def city(ctx):
    await ctx.send("я хотов, пиши города на русскому языке с заглавной буквы")
    used_cities = []

@client.command()
async def start(ctx):
    await ctx.send("вы начали игру, напишите название любого города")
    steps.append(BOT_NAME)

@client.command()
async def step(ctx, city):
    if len(steps) == 0:
        await ctx.send("Чтобы начать игру напишите !start")
        return
    
    if ctx.author == steps[-1]:
        return

    if ctx.author != BOT_NAME:
        await user_step(ctx, city)        
    await bot_step(ctx)
        
print(os.environ['TOKEN'])
client.run(os.environ['TOKEN'])