
import discord, yaml, requests
from discord.ext import commands
from arr import SonarrAPI

with open("config.yml", "r") as ymlfile:
    try:
        config = yaml.safe_load(ymlfile)
    except yaml.YAMLError as exc:
        print(exc)

sonarrHost = config['sonarr']['host']
sonarrToken = config['sonarr']['token']
sonarr = SonarrAPI(sonarrHost, sonarrToken)

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
        """- Show tatus of your Sonarr instance."""
        sysStatus = sonarr.get_system_status

        await ctx.send()

def setup(bot):
    bot.add_cog(Sonarr(bot))
