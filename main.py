import json
import os
import random
import discord
from discord.ext import commands
from termcolor import colored

bot = commands.Bot(command_prefix='=', intents=discord.Intents.all())
bot.remove_command('help')


@bot.event
async def on_ready():
    print(colored(f'Botid: {bot.user.id} - Name: {bot.user.name}', 'green'))
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name='Social Score'),
        status=discord.Status.idle)


@bot.command(name='social', aliases=['score', 'social_score'])
async def social_score(ctx):
    """Give you a random generated Social Score back"""
    with open('social_score.json', 'r') as f:
        data = json.load(f)

    social_score_memes = data['social_score']
    meme = random.choice(social_score_memes)

    embed = discord.Embed(description=f'{ctx.author.mention} has got a social score!')
    embed.set_image(url=meme)
    embed.set_author(name=f'{ctx.author.name}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

bot.run('your token')
