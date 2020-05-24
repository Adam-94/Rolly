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

@client.command()
async def roll(ctx, user_post):

    dice_over = [ "My dice bag isn't that big :(",
                  "Laura Bailey stole all the dice",
                  "I don't own a bag of holding",
                  "That is too many dice sir...",
                ]

    get_roll = 0
    roll = 0
    modifier = 0
    total = 0
    die_amount = []
    die = []
    
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


    get_roll = [random.randint(1, die) for _ in range(die_amount)]
    n = len(get_roll)
    for i in range(n):
        roll += get_roll[i]

    total = roll + modifier
    if die == 20 and roll == 20: 
        roll = str("Natural 20!")
    if die == 20 and roll == 1: 
        roll = str("Critical 1!")

    if die_amount > 99: 
        await ctx.send(random.choice(dice_over))
    elif modifier > 0: 
        await ctx.send(f'Rolling {die_amount}d{die}+{modifier}\nYou rolled: {get_roll}\nTotal: {total}')
    elif die_amount > 1:
        await ctx.send(f'Rolling {die_amount}d{die}\nYou rolled: {get_roll}\nTotal: {total}')
    else: 
        await ctx.send(f'Rolling {die_amount}d{die}\nYou rolled: {total}')
client.run(TOKEN)
