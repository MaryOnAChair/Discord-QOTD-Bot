import discord

qfile = 'listOfSuggestedQuestions.txt'
def addToSuggested(userSuggestion):
    with open(qfile ,'a' ) as file:
        file.writelines(userSuggestion)
        file.close()