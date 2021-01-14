import logging
import discord_bot
import settings as settings

logging.basicConfig(level=logging.INFO)




logging.info(
    f"Hey I'm a bot!"
)

discord_bot.run_discordbot(settings.DISCORD_API_TOKEN)

