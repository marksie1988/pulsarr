import discord, asyncio, yaml, requests
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

class arrCommands(commands.Cog, name='Arr'):
    """All Sonarr & Radarr related commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def status(self, ctx):
        """Show status of your Sonarr instance."""
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

        await ctx.send(embed=stautsEmbed)

    @commands.command()
    async def diskSpace(self, ctx):
        """Show diskspace of your Sonarr instance."""
        diskSpace = sonarr.get_diskspace()

        def GetHumanReadable(size,precision=2):
            suffixes=['B','KB','MB','GB','TB']
            suffixIndex = 0
            while size > 1024 and suffixIndex < 4:
                suffixIndex += 1 #increment the index of the suffix
                size = size/1024.0 #apply the division
            return "%.*f%s"%(precision,size,suffixes[suffixIndex])

        embedColour = discord.Colour.green()

        for disk in diskSpace:
            freePct = (disk['freeSpace'] / disk['totalSpace'] * 100)
            if freePct < 10:
                embedColour = discord.Colour.red()

        diskEmbed = discord.Embed(
            title = 'Disk Usage',
            description = '',
            colour = embedColour
        )

        for disk in diskSpace:
            path = disk['path']
            space = GetHumanReadable(disk['freeSpace'])
            total = GetHumanReadable(disk['totalSpace'])
            diskEmbed.add_field(name='Path', value=path, inline=True)
            diskEmbed.add_field(name='Free Space', value=space, inline=True)
            diskEmbed.add_field(name='Total Space', value=total, inline=True)
            await ctx.send(embed=diskEmbed)

    @commands.command()
    async def search(self, ctx, mediaType, *args):
        """Lookup a series based on a search term"""
        if len(args) <= 1:
            await ctx.send('search requires `search <movie|series> <"the title"|tvdb-id>`\n')
        elif mediaType == 'series':
            term = "%20".join(args)

            lookup = sonarr.lookup_series(term)
            print(lookup)
            if len(lookup)==0:
                formattedResults = "No records were returned for that search.\n"
            else:
                formattedResults = "Here are your search results for `" + term.replace('%20', ' ') + "`:\n"

                for result in lookup:
                    formattedResults += "- " + result['title'] + " (" + str(result['year']) + ") `" + str(result['tvdbId']) + "`\n"

            await ctx.send(formattedResults)

        elif mediaType == 'movie':
            await ctx.send('Radarr movies not implemented yet')
        else:
            await ctx.send('search requires `search <movie|series> <"the title"|tvdb-id>`\n')

def setup(bot):
    bot.add_cog(arrCommands(bot))
    print('arrCommands is loaded')