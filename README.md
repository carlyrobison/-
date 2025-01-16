# 🚿🍈🤖

## Why?
Automating some of the tedium of organizing when we unlock a new puzzle can free up our energy for solving.

## What?
Miscellaneous bot and code for the Shower Pomelo MIT Mystery Hunt team.

Pieces:
- Discord bot
- Google Sheets integration
- Hosted online (currently set up for Heroku)
- (TODO) Code repository for those puzzles that need it
- (In progress) Knowledge repository

Planned improvements are tracked as GitHub Issues.

### Discordbot
- Command for new puzzle creates google sheet, new channel, publishes link to sheet, pings @new puzzle in channel, and informs hub
- Command for solving a puzzle marks and moves the Google sheet, moves the Discord channel to the archive, and informs Hub
- Use `$help` to list current commands

### Google Sheets integration
- Shared folder needed
- Uses a service account
- Makes a copy of a template sheet, names it, puts it in the applicable folder
- Updates the title of the sheet when solved

### Hosted online somewhere
- Currently on free tier of Heroku.
- Can also run in Docker, see below:

### Code repository for those puzzles that need it
Commonly used functions (assuming python):
- CSV to Numpy array
- Alphabetic 1=A 26=Z encoding
- Basic anagrammer
- SAT solver
- Grid game model?

## Docker

### Build

```bash
docker build -t carlyrobison/shower-pomelo-bot:latest .
```

### Push

```bash
docker push carlyrobison/shower-pomelo-bot:latest
```

## Secrets

Running in k8s requires the following secret to be created:

```bash
kubectl create secret generic gcp \
--from-literal=GOOGLE_DRIVE_HUNT_FOLDER_ID= \
--from-literal=GOOGLE_DRIVE_SOLVED_FOLDER_ID= \
--from-literal=GOOGLE_SHEETS_TEMPLATE_FILE_ID= \
--from-literal=DISCORD_PUZZLEANNOUNCE_CHANNEL= \
--from-literal=DISCORD_PUZZLE_CATEGORY= \
--from-literal=DISCORD_ARCHIVE_CATEGORY= \
--from-literal=GOOGLE_API_CLIENT_EMAIL= \
--from-literal=GOOGLE_API_PRIVATE_KEY= 
```