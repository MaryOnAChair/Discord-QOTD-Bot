from email import message
import string
import discord
from discord.ext import commands,tasks
from dotenv import load_dotenv
import os
from timeHandler import MyCog
from fileHandler import getQOTD,updateUsedQuestions
from questionHandler import addToSuggested

load_dotenv('.env.txt') # loads .env file
bot_key = os.getenv('botKey') # gets bot key from .env file

CHANNEL_ID = 966211020064444456  # Assigns static channel name, -> Will be changed
bot = commands.Bot(command_prefix='$',intents=discord.Intents.all()) # Creates bot


 # When Bot first starts
@bot.event
async def on_ready():
    print("I'm in")
    print(bot.user)
    MyCog(bot)

# Responds to User DM and user DM only
@bot.command()
async def ping(ctx):
    if isinstance(ctx.channel,discord.channel.DMChannel):
        await ctx.send('pong')

@bot.command()
async def  addQuestion(ctx):
        if isinstance(ctx.channel,discord.channel.DMChannel):
            addToSuggested(ctx.message.content)
            await ctx.send('Processing Question Beep Boop')

bot.run(bot_key) # Runs Dave :)