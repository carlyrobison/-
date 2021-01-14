

class Command:
	# Takes an invocation, e.g. "!new_puzzle",
	# explanation, e.g. "Makes a new puzzle spreadsheet and channel. Format !new_puzzle {name} {url} without the braces"
	# and invocation, which is a function that takes the whole message, parses it, and does the described things.
	def __init__(self, invocation, explanation, fxn):
		self.invocation = invocation
		self.explanation = explanation
		self.fxn = fxn

	def display():
		return self.invocation + ":\t" +  self.explanation

	async def invoke(msg):
		return await self.fxn(msg)

	def matches(message):
		return message.startswith(self.invocation)


DATA_MODEL = """
Shower Pomelo Bot is a discord-first bot for creating puzzle solving spreadsheets. It has two main functions:
- !new_puzzle
- !solve_puzzle

In the event that it fails, you can perform the equivalent steps manually.

For new_puzzle:
1. Duplicate the template spreadsheet (rename it to something relevant)
2. Make a new Discord chat channel in the PUZZLES category
3. Store the spreadsheet link (in the channel description? pins?)
4. Announce the new puzzle in the hub channel!

When you are solving, feel free to make subfolders for rounds and categories if it is helpful.

For solve_puzzle:
1. Move the spreadsheet to the SOLVED folder
2. Move the discord channel to the ARCHIVED category
3. Announce in the general channel that a puzzle has been solved!

There's also some helper functions:
- !help (lists commands)
- !datamodel (lists this)
- !summary (lists number of puzzles(sheets) outstanding and number of puzzles in the archive folder)
"""
