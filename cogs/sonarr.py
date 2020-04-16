
import discord, yaml, requests
from discord.ext import commands
from PyArr import SonarrAPI

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
        """- Show status of your Sonarr instance."""
        sysStatus = sonarr.get_system_status()
        stautsEmbed = discord.Embed(
            title = 'Sonarr Status',
            description = '',
            colour = discord.Colour.blue()
        )
        ver = sysStatus['version']
        debug = sysStatus['isDebug']
        if sysStatus['isProduction'] == True: 
            stautsEmbed.add_field(name='Status', value='In Production', inline=False)
        stautsEmbed.add_field(name='Debug Enabled', value=debug, inline=False)
        stautsEmbed.set_footer(text=f'Sonarr Version: {ver}')
        print(sysStatus)
        await ctx.send(embed=stautsEmbed)

    @commands.command()
    async def diskSpace(self, ctx):
        """- Show diskspace of your Sonarr instance."""
        with sonarr.get_diskspace() as diskSpace:
            for disk in diskSpace:
                print(disk)
                path = disk['path']
                space = disk['freespace']
                total = disk['totalspace']

                diskEmbed = discord.Embed(
                    title = f'{path} Usage',
                    description = '',
                    colour = discord.Colour.blue()
                )
                diskEmbed.add_field(name='Free Space', value=space, inline=False)
                diskEmbed.add_field(name='Total Space', value=total, inline=False)
                await ctx.send(embed=diskEmbed)

def setup(bot):
    bot.add_cog(Sonarr(bot))
