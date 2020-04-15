
import discord, yaml, requests
from discord.ext import commands
from .arr.sonarr_api import SonarrAPI

with open("config.yml", "r") as ymlfile:
    try:
        config = yaml.safe_load(ymlfile)
    except yaml.YAMLError as exc:
        print(exc)

sonarrHost = config['sonarr']['host']
sonarrToken = config['sonarr']['token']

with open("config.yml", "r") as ymlfile:
    try:
        config = yaml.safe_load(ymlfile)
    except yaml.YAMLError as exc:
        print(exc)

class Sonarr(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def status(self, ctx):
        """Show example of connecting to your Sonarr instance."""
        async with Sonarr(sonarrHost, sonarrToken) as sonarr:
            info = sonarr.update()
            await ctx.send(info)

def setup(bot):
    bot.add_cog(Sonarr(bot))
