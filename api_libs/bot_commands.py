import settings as settings
import google_api
import usage

gDrive = google_api.GoogleDriveAPI()

def convert_to_server_friendly_name(title):
	# TODO parsed "Rick's on a Roll" as "onaroll", maybe have to specify split('')?
	title = title.split()
	title = ['_' if c == ' ' else c for c in title] # convert spaces to underscores
	title = [c if c.isalpha() else '' for c in title]
	title = ''.join(title)
	if len(title) < 1:
		raise NameError('Must provide a name that has some alphabetic characters')
	return title

# here commences all the commands
async def new_puzzle(client, message):
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
	# TODO suppress link previews
	conclusion_message += "Your sheet is now available at: " + sheet_url
	await new_channel.send(conclusion_message)

	return await message.channel.send("New puzzle created. See channel #{0} for details".format(new_channel))

async def solve_puzzle(client, message):
	await message.channel.send('Solved puzzle request detected!')

	answer = message.content[13:]
	print('answer', answer)

	# Get the spreadsheet url from the channel topic
	sheet_url = message.channel.topic # we hope nobody changed it
	if sheet_url is None or sheet_url == '':
		await message.channel.send('Unable to detect spreadsheet url, please move spreadsheet manually')
	else: # Move the spreadsheet to the SOLVED folder
		gDrive.solve_sheet(sheet_url, answer);
	# Move the discord channel to the ARCHIVED category (TODO)
	for cat in message.guild.categories: # TODO optimize
		if cat.name == settings.DISCORD_ARCHIVE_CATEGORY:
			await message.channel.edit(category=cat)
			break

	# Announce in the general channel that a puzzle has been solved! (TODO)
	announce_channel = client.get_channel(int(settings.DISCORD_PUZZLEANNOUNCE_CATEGORY))
	return await announce_channel.send('Puzzle {0} solved!'.format(message.channel));

async def datamodel(client, message):
	return await message.channel.send(usage.DATA_MODEL)

async def debug_info(client, message):
	print(message.channel, message.channel.category, message.guild, message.content)
	return await message.channel.send('channel: {0}, category: {1}'.format(message.channel, message.channel.category))

# - $help (lists commands) [TODO]
# - $summary (lists number of puzzles(sheets) outstanding and number of puzzles in the archive folder) [TODO]
# - $debug_info (lists current channel id and category id in debug)

COMMANDS = [
	usage.Command("$new_puzzle", "Makes a new puzzle spreadsheet and channel. Format '$new_puzzle Name Of Puzzle http(s)://puzzle_link'", new_puzzle),
	usage.Command("$solve_puzzle", "Solves the puzzle and archives the current channel and spreadsheet in the description. Format '$solve_puzzle answer' in the relevant channel", solve_puzzle),
	usage.Command("$datamodel", "Describes the data model and how to do the bot functions if the bot is down", datamodel),
	usage.Command("$debug_info", "Lists debug info", debug_info),
	]


