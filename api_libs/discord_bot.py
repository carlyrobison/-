import discord
import google_api

client = discord.Client()

# when bot is ready to be used
@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

# gets a message
@client.event
async def on_message(message):
	# don't do anything if it's from us
	if message.author == client.user:
		return

	# if starts with command
	if message.content.startswith('!make_puzzle'):
		await message.channel.send('Puzzle creation request detected!')

		print(google_api.make_sheet('My Fabulous Spreadsheet')) # add url

		await message.channel.send('Puzzle created')

	# if starts with command
	elif message.content.startswith('!'):
		await message.channel.send("Command detected, but I'm not sure what to do with it.")



def run_discordbot(API_TOKEN):
	google_api.make_sheet('My Fabulous Spreadsheet')

	client.run(API_TOKEN)
