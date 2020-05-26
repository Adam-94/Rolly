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
    modifier = ""
    total = 0
    die_amount = []
    die = []
    plus_or_minus = None

    user_request = list(user_post)
    n = len(user_request)
    command_index = user_request.index('d')

    if '+' in user_request:
        plus_or_minus = True
        index = user_request.index('+')
    elif '-' in user_request:
        plus_or_minus = False
        index = user_request.index('-')

    """extract modifier"""
    if plus_or_minus == True or plus_or_minus == False:
        for i in range(index,n):
            if user_request[i].isdigit():
               modifier += "".join(list(user_request[i]))
            
        """remove + and modifier from list""" 
        if len(modifier) == 2:
            del user_request[-3:]
        elif len(modifier) == 1:
            del user_request[-2:]

        modifier = int(modifier)
         
          
    """Getting die amount and then removing from list"""
    for index in range(0, command_index):
        die_amount.append(user_request[index])
        user_request.pop(index)
    user_request.remove('d')

    die = int("".join(user_request))
    die_amount = int("".join(die_amount))

    get_roll = [random.randint(1, die) for _ in range(die_amount)]
    n = len(get_roll)

    if die == 20 and die_amount > 1:
        high = max(get_roll)
        low = min(get_roll)
        if modifier != "" and plus_or_minus == True:
            high += modifier
            low += modifier
        else:
            high -= modifier
            low -= modifier
            
   
    for i in range(n):
        roll += get_roll[i]
    
    if plus_or_minus == True:
        roll += modifier
    else:
        roll -= modifier

    if die == 20 and 20 in get_roll: 
        index = get_roll.index(20)
        get_roll[index] = str("Natural 20!")
    if die == 20 and 1 in get_roll:
        index = get_roll.index(1) 
        get_roll[index] = str("Critical 1!")

    
    if die_amount > 99: 
        await ctx.send(random.choice(dice_over))
    
    elif die == 20 and die_amount == 2:
        await ctx.send(f'Rolling {user_post}\nYou rolled: {get_roll}\nTotal high: {high}\nTotal low: {low}')
    
    elif die_amount == 1 and modifier != "": 
        await ctx.send(f'Rolling {user_post}\nYou rolled: {get_roll}\nTotal: {roll}')
    
    elif die_amount > 1:
        await ctx.send(f'Rolling {user_post}\nYou rolled: {get_roll}\nTotal: {roll}')
    
    else: 
        await ctx.send(f'Rolling {user_post}\nYou rolled: {roll}')
client.run(TOKEN)
