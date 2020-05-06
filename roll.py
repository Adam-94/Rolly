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

def get_dice_info(dice_amount = [], die = []):
    dice_amount = int("".join(dice_amount))
    die = int("".join(die))

    return dice_amount, die

@client.command()
async def roll(ctx, user_post):
    get_roll = 0
    n_die = 0
    n_die_amount= 0 
    die_amount = []
    die = []
    

    user_request = [char for char in user_post]
    command_index = user_request.index('d')
    print(command_index, '\n')

    for index in range(0, command_index):
        die_amount.append(user_request[index])

    for index in range(command_index+1, len(user_request)):
        die.append(user_request[index])

    n_die_amount, n_die = get_dice_info(die_amount, die)
    print("Die amount: ", n_die_amount, "\nDie: ", n_die)
        
    if n_die_amount < 100:
        get_roll = random_dice(n_die_amount, n_die)

    if n_die == 20 and get_roll == 20: get_roll = str("Natural 20!")
    if n_die == 20 and get_roll == 1: get_roll = str("Critical 1!")
    
    if n_die_amount > 99: await ctx.send("My dice bag isn't that big :(")
    else: await ctx.send(f'Rolling {n_die_amount}d{n_die}\nYou rolled: {get_roll}')

client.run(TOKEN)