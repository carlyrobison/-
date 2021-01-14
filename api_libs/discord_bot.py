import discord
import google_api
import usage
import settings as settings

client = discord.Client()
gDrive = google_api.GoogleDriveAPI()

# when bot is ready to be used
@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

def convert_to_server_friendly_name(title):
	title = title.split()
	title = ['_' if c == ' ' else c for c in title] # convert spaces to underscores
	title = [c if c.isalpha() else '' for c in title]
	title = ''.join(title)
	if len(title) < 1:
		raise NameError('Must provide a name that has some alphabetic characters')
	return title


# here commences all the commands
async def new_puzzle(message):
	await message.channel.send('New puzzle request detected!')

	conclusion_message = ""

	msg_bits = message.content.split(' ')
	# check for insufficient data
	if len(msg_bits) < 2:
		return await message.channel.send(' Not enough info sent. Please specify a name and url')

	# extract url
	# TODO: refactor with Discord Commands https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html
	print(msg_bits)
	msg_url = msg_bits[-1]
	if not msg_url.startswith('http'):
		conclusion_message += "No url found, fine. Add it later on the spreadsheet if applicable.\n"
		msg_url = ''
		puzzle_name = ' '.join(msg_bits[1:])
	else:
		puzzle_name = ' '.join(msg_bits[1:-1])

	print("puzzle url:", msg_url, "puzzle name", puzzle_name)
	conclusion_message += "Making spreadsheet for puzzle named: " + puzzle_name + " at url: " + msg_url + "\n"

	# Make a new discord Channel in the right category
	server_friendly_name = convert_to_server_friendly_name(puzzle_name)
	print(message.guild.categories)
	new_channel = None
	for cat in message.guild.categories: # TODO optimize
		if cat.name == settings.DISCORD_PUZZLE_CATEGORY:
			new_channel = await message.guild.create_text_channel(server_friendly_name, category=cat)
			break
	print(new_channel)

	# TODO add link to discord channel on spreadsheet. Also put title into sheet
	sheet_url = gDrive.make_sheet(puzzle_name, msg_url)


	# Update new discord channel with data
	await new_channel.edit(topic=sheet_url, reason='Made new channel')
	conclusion_message += "Your sheet is now available at: " + sheet_url
	await new_channel.send(conclusion_message)

	return await message.channel.send("New puzzle created. See channel #{0} for details".format(new_channel))


commands = [usage.Command("!new_puzzle", "Makes a new puzzle spreadsheet and channel. Format '!new_puzzle Name Of Puzzle http(s)://puzzle_link'", new_puzzle)]



# gets a message
@client.event
async def on_message(message):
	# don't do anything if it's from us
	if message.author == client.user:
		return

	if message.content.startswith('!debug_info'):
		print(message.channel, message.channel.category, message.guild, message.content)

	# if starts with command
	if message.content.startswith('!new_puzzle'):
		await message.channel.send('Puzzle creation request detected!')

		# try:
		await new_puzzle(message) # add url
		# except (NameError, TypeError) as e:
		# 	print('Error: {0}'.format(e))
		# 	await message.channel.send('Error: {0}'.format(e))
		# except:
		# 	await message.channel.send('Something else went wrong.')

		# await message.channel.send('Puzzle created')

	# if starts with command
	elif message.content.startswith('!'):
		await message.channel.send("Command detected, but I'm not sure what to do with it.")



def run_discordbot(API_TOKEN):
	client.run(API_TOKEN)
