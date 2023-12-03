
import discord
from discord.ext import tasks, commands
import faked_settings as settings

DELAY_MINUTES_BEFORE_PING = 1

class MyReminders(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def setup_hook(self) -> None:
        self.remind_to_update.start()

    
    @tasks.loop(minutes = 1)
    async def remind_to_update(self):
        print("Looping!")
        for channel in self.text_channels():
            # SKIP: check if text channel -- if not continue
            # Get the latest message to the channel
            message = channel.last_message
            if (message): # since it's optional
                # Check if shower pomelo bot was the last messager -- if so continue
                if message.author.id == 799210529884733450:
                    continue

                # check if the last message started with "status": if so continue
                if message.content.startsWith("status:"):
                    continue

                # else ping this channel if 5 minutes have elapsed
                if message.

            # channel = self.get_channel(int(settings.DISCORD_PUZZLEANNOUNCE_CHANNEL))
        

        await channel.send("Reminder! Please update the channels of puzzles you have worked on.")
    

    @remind_to_update.before_loop
    async def before_remind_to_update(self):
        await tasker.wait_until_ready()
        print("Ready now!")

tasker = MyReminders(intents=discord.Intents.all())