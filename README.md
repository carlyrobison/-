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

### Google Sheets integration
- Shared folder needed
- Uses a service account
- Makes a copy of a template sheet, names it, puts it in the applicable folder
- Updates the title of the sheet when solved

### Hosted online somewhere
- Currently on free tier of Heroku

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