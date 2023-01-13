
import discord
from discord.ext import tasks, commands
import faked_settings as settings

class MyReminders(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def setup_hook(self) -> None:
        self.remind_to_update.start()

    
    @tasks.loop(hours = 1)
    async def remind_to_update(self):
        print("Looping!")
        channel = self.get_channel(int(settings.DISCORD_PUZZLEANNOUNCE_CHANNEL))
        await channel.send("Reminder! Please update the channels of puzzles you have worked on.")
    

    @remind_to_update.before_loop
    async def before_remind_to_update(self):
        await tasker.wait_until_ready()
        print("Ready now!")

tasker = MyReminders(intents=discord.Intents.all())