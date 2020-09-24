#!/usr/bin/env python3

import discord
import random
import os
import io

from search import screenshot
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
async def find(ctx, user_post):
    if "_" in user_post:
        user_post = user_post.replace("_", "%20")
        print(user_post)
    screenshot(user_post)
    await ctx.send(file=discord.File('screenshot.png'))

def die_info(user_message):
    die_amount = []
    die = []
    modifer = []

    plus_or_minus = False
    modifer_index = 0
    
    user_request = list(user_message)
    n = len(user_request)
    d_prefix = user_request.index('d')
    
    if '+' in user_request:
        plus_or_minus = True
        modifer_index = user_request.index('+')
    elif '-' in user_request:
        plus_or_minus = False
        modifer_index = user_request.index('-')
    else:
        plus_or_minus = None

    if plus_or_minus != None:
        for digits in range(modifer_index+1, n):
            modifer.append(user_request[digits])
        
    # Die amount
    for digits in range(0, d_prefix):
        die_amount.append(user_request[digits])
        
    # Die 
    if plus_or_minus == None:
        for digits in range(d_prefix+1, n):
            die.append(user_request[digits])
        modifer.append(0)
    else:
        for digits in range(d_prefix+1, modifer_index):
            die.append(user_request[digits])
        
    # Concatonating lists into integers
    die_amount = int(''.join(map(str, die_amount)))
    die = int(''.join(map(str, die)))
    modifer = int(''.join(map(str, modifer)))
    

    return die_amount, die, modifer

@client.command()
async def roll(ctx, user_message):

    dice_over = [ "My dice bag isn't that big :(",
                  "Laura Bailey stole all the dice",
                  "I don't own a bag of holding",
                  "That is too many dice sir...",
                ]
    die_amount = 0
    modifier = 0
    die = 0

    get_roll = 0
    roll = 0
    total = 0

    die_amount, die, modifier = die_info(user_message)
    if die_amount > 99:
        await ctx.send(random.choice(dice_over))
        return 1

    get_roll = [random.randint(1, die) for _ in range(die_amount)]
    roll = sum(get_roll)

    if die == 20 and die_amount > 1:
        high = max(get_roll)
        low = min(get_roll)
        if modifier > 0:
            high += modifier
            low += modifier
        else:
            high -= modifier
            low -= modifier

    roll += modifier

    if die_amount == 1 and die == 20 and 20 in get_roll:
        index = get_roll.index(20)
        get_roll[index] = str("Natural 20!")
        roll = str("Natural 20!")
    if die_amount == 1 and die == 20 and 1 in get_roll:
        index = get_roll.index(1)
        get_roll[index] = str("Critical 1!")
        roll = str("Critical 1!")

    elif die == 20 and die_amount == 2:
        await ctx.send(f'Rolling {user_message}\nYou rolled: {get_roll}\nTotal high: {high}\nTotal low: {low}')

    elif die_amount == 1 and modifier != "":
        await ctx.send(f'Rolling {user_message}\nYou rolled: {get_roll}\nTotal: {roll}')

    elif die_amount > 1:
        await ctx.send(f'Rolling {user_message}\nYou rolled: {get_roll}\nTotal: {roll}')

    else:
        await ctx.send(f'Rolling {user_message}\nYou rolled: {roll}')


client.run(TOKEN)
