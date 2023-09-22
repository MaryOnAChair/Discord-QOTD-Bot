import datetime
from discord.ext import commands,tasks
from fileHandler import getQOTD,updateUsedQuestions

utc = datetime.timezone.utc

# If no tzinfo is given then UTC is assumed.
time = datetime.time(hour=23, minute=36, tzinfo=utc

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.my_task.start()

    def cog_unload(self):
        self.my_task.cancel()

    @tasks.loop(time=time)
    async def my_task(self):
        print("My task is running!")
        channel = self.bot.get_channel(1146189271691182160)
        await channel.send(getQOTD())





    
    

