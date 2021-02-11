#!/usr/bin/env python3

import discord
import random
import os
import io
import re
import sys


from search import screenshot
from dotenv import load_dotenv, find_dotenv
from discord.ext import commands

random.seed()
load_dotenv()
TOKEN = os.getenv("TOKEN")

client = commands.Bot(command_prefix="-")


@client.event
async def on_ready():
    print("Bot is ready!")


@client.command()
async def find(ctx, user_post):
    if "_" in user_post:
        user_post = user_post.replace("_", "%20")
        print(user_post)
    screenshot(user_post)
    await ctx.send(file=discord.File("screenshot.png"))


@client.command()
async def purge(ctx):
    def not_pinned(msg):
        return not msg.pinned

    purged = await ctx.channel.purge(limit=100, check=not_pinned)
    await ctx.send(f"Successfully removed {len(purged)} non-pinned messages!")


@client.command()
async def roll(ctx, user_message):
    pattern = re.compile(
        r"(?P<amount>[0-9]+)([dD])(?P<sides>[0-9]+)?(?P<mod>[+-])?(?P<val>[0-9]+)?"
    )

    match = re.match(pattern, user_message)
    if not match:
        raise ValueError()

    amount = int(match.group("amount"))
    sides = int(match.group("sides"))
    plus_or_minus = str(match.group("mod"))

    try:
        modifier = int(match.group("val"))
    except:
        modifier = None

    if plus_or_minus == "+":
        plus_or_minus = True
    elif plus_or_minus == "-":
        plus_or_minus = False

    if amount > 1:
        await ctx.send(multi_roll(amount, sides, plus_or_minus, modifier))
    else:
        await ctx.send(single_roll(sides, plus_or_minus, modifier))


def single_roll(sides, plus_or_minus, modifier):
    roll = random.randint(1, sides)
    if plus_or_minus is not None:
        total = 0

    if plus_or_minus == True:
        total = roll + modifier
        return f"You rolled: {roll}\nTotal Roll: {total}"

    elif plus_or_minus == False:
        total = roll - modifier
        return f"You rolled: {roll}\nTotal Roll: {total}"
    else:
        return f"You rolled: {roll}"


def multi_roll(amount, sides, plus_or_minus, modifier):
    roll = [random.randint(1, sides) for _ in range(amount)]
    if plus_or_minus is not None:
        total = []

    if plus_or_minus == True:
        total = [num + modifier for num in roll]
        return f"You rolled: {*roll,}\nTotal Roll: {*total,}"
    elif plus_or_minus == False:
        total = [num - modifier for num in roll]
        return f"You rolled: {*roll,}\nTotal Roll: {*total,}"
    else:
        return f"You rolled: {*roll,}"


client.run(TOKEN)
