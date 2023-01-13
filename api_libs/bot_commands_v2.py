import settings as settings
import google_api
import usage
from discord.ext import commands

gDrive = google_api.GoogleDriveAPI()

# PUBLIC_COMMANDS = [
# 	usage.Command("$new_puzzle", "Makes a new puzzle spreadsheet and channel. Format '$new_puzzle Name Of Puzzle <http(s)://puzzle_link>', link optional", new_puzzle),
# 	usage.Command("$solve_puzzle", "Solves the puzzle and archives the current channel and spreadsheet in the description. Format '$solve_puzzle answer' in the relevant channel", solve_puzzle),
# 	usage.Command("$datamodel", "Describes the data model and how to do the bot functions if the bot is down", datamodel),
# ]

# async def help_cmd(client, message):
# 	return await message.channel.send('\n'.join([c.display() for c in PUBLIC_COMMANDS]))

bot = commands.Bot(command_prefix='$')

@bot.command()
async def datamodel(ctx, args):
    return await ctx.send(usage.DATA_MODEL)

bot.add_command(datamodel)