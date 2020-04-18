import discord, asyncio, os, yaml
from discord.ext import commands

with open("config.yml", "r") as ymlfile:
    try:
        config = yaml.safe_load(ymlfile)
    except yaml.YAMLError as exc:
        print(exc)

BOT_NAME = config['botName']
BOT_TOKEN = config['botToken']
BOT_PREFIX = config['botPrefix']

# TODO: add mongodb with guilds for server specific prefixes
def get_prefix(bot, message):
    if not message.guild: 
        return commands.when_mentioned_or("/pulsarr ")(bot, message)
    else:
        return commands.when_mentioned_or(BOT_PREFIX)(bot, message)

bot = commands.Bot(command_prefix = get_prefix, case_insensitive=True)
bot.remove_command('help')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(BOT_TOKEN)
