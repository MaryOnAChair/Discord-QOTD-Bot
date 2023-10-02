import discord
from discord.ext import commands


qfile = 'listOfSuggestedQuestions.txt'
def addToSuggested(userSuggestion):
    with open(qfile ,'a' ) as file:
        file.writelines(userSuggestion + "\n")
        file.close()


