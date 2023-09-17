import string
import discord
from discord.ext import commands,tasks
from dotenv import load_dotenv
import os

from fileHandler import getQOTD,updateUsedQuestions

 

load_dotenv('.env.txt') # loads .env file
bot_key = os.getenv('botKey') # gets bot key from .env file

CHANNEL_ID = 1146189271691182160  # Assigns static channel name, -> Will be changed
bot = commands.Bot(command_prefix='$',intents=discord.Intents.all()) # Creates bot


 # When Bot first starts
@bot.event
async def on_ready():
    print("I'm in")
    print(bot.user)
    test = getQOTD()

bot.run(bot_key) # Runs Dave :)