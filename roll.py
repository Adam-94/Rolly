import discord
import random
import os
from dotenv import load_dotenv, find_dotenv
from discord.ext import commands

random.seed()
load_dotenv()
TOKEN = os.getenv('TOKEN')

client = commands.Bot(command_prefix= "-")

@client.event
async def on_ready():
    print("Bot is ready!")

def random_dice(die_amount, die):
    get_roll = [random.randint(1, die) for _ in range(die_amount)]
    print(len(get_roll))

    total_roll = 0
    for i in range(len(get_roll)):
        print(get_roll[i])
        total_roll += get_roll[i]

    return total_roll

@client.command()
async def roll(ctx, user_post):

    dice_over = [ "My dice bag isn't that big :(",
                  "Laura Bailey stole all the dice",
                  "I don't own a bag of holding",
                  "That is too many dice sir...",
                ]

    get_roll = 0
    die_amount = []
    die = []
    modifier = []


    user_request = list(user_post)
    command_index = user_request.index('d')
    if '+' in user_request:
        modifier = int("".join(list(user_request.pop())))
    user_request.pop()

    """Getting die amount and then removing from list"""
    for index in range(0, command_index):
        die_amount.append(user_request[index])
        user_request.pop(index)
    user_request.remove('d')

    die = int("".join(user_request))
    die_amount = int("".join(die_amount))


    if die_amount > 1 and die_amount < 100:
        get_roll = random_dice(die_amount, die)

    if die == 20 and get_roll == 20: 
        get_roll = str("Natural 20!")
    if die == 20 and get_roll == 1: 
        get_roll = str("Critical 1!")

    if die_amount > 99: 
        await ctx.send(random.choice(dice_over))
    elif modifier > 0: 
        await ctx.send(f'Rolling {die_amount}d{die}\nYou rolled: {get_roll}\nTotal: {modifier+get_roll}')
    else: 
        await ctx.send(f'Rolling {die_amount}d{die}\nYou rolled: {get_roll}')
client.run(TOKEN)
