import discord
import google_api
import usage

client = discord.Client()
gDrive = google_api.GoogleDriveAPI()

# when bot is ready to be used
@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))


# here commences all the commands
async def new_puzzle(msg, channel):
	conclusion_message = ""

	msg_bits = msg.split(' ')
	# check for insufficient data
	if len(msg_bits) < 2:
		return await channel.send(' Not enough info sent. Please specify a name and url')

	# extract url
	print(msg_bits)
	msg_url = msg_bits[-1]
	if not msg_url.startswith('http'):
		conclusion_message += "No url found, fine. Add it later on the spreadsheet if applicable"
		msg_url = ''
		puzzle_name = ' '.join(msg_bits[1:])
	else:
		puzzle_name = ' '.join(msg_bits[1:-1])

	print("puzzle url:", msg_url, "puzzle name", puzzle_name)
	conclusion_message += "Making spreadsheet for puzzle named: " + puzzle_name + " at url: " + msg_url + "\n"

	sheet_url = gDrive.make_sheet(puzzle_name, msg_url)

	conclusion_message += "Your sheet is now available at: " + sheet_url

	return await channel.send(conclusion_message)


commands = [usage.Command("!new_puzzle", "Makes a new puzzle spreadsheet and channel. Format '!new_puzzle Name Of Puzzle http(s)://puzzle_link'", new_puzzle)]





# gets a message
@client.event
async def on_message(message):
	# don't do anything if it's from us
	if message.author == client.user:
		return

	# if starts with command
	if message.content.startswith('!new_puzzle'):
		await message.channel.send('Puzzle creation request detected!')

		try:
			await new_puzzle(message.content, message.channel) # add url
		except NameError, TypeError as e:
			await message.channel.send('Error: {0}'.format(e))
		except:
			await message.channel.send('Something else went wrong.')

		await message.channel.send('Puzzle created')

	# if starts with command
	elif message.content.startswith('!'):
		await message.channel.send("Command detected, but I'm not sure what to do with it.")



def run_discordbot(API_TOKEN):
	client.run(API_TOKEN)
