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

    def GetHumanReadable(size,precision=2):
        suffixes=['B','KB','MB','GB','TB']
        suffixIndex = 0
        while size > 1024 and suffixIndex < 4:
            suffixIndex += 1 #increment the index of the suffix
            size = size/1024.0 #apply the division
        return "%.*f%s"%(precision,size,suffixes[suffixIndex])

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
            space = self.GetHumanReadable(disk['freeSpace'])
            total = self.GetHumanReadable(disk['totalSpace'])
            diskEmbed.add_field(name='Path', value=path, inline=True)
            diskEmbed.add_field(name='Free Space', value=space, inline=True)
            diskEmbed.add_field(name='Total Space', value=total, inline=True)
            await ctx.send(embed=diskEmbed)

    @commands.command()
    async def getfolder(self, ctx, mediaType):
        """Get the default directory for media storage"""
        if mediaType == 'series':
            embedColour = discord.Colour.green()
            rootFolder = sonarr.get_root_folder()

            for root in rootFolder:
                freePct = round((root['freeSpace'] / root['totalSpace'] * 100), 2)
                if freePct < 10:
                    embedColour = discord.Colour.red()

            diskEmbed = discord.Embed(
                title = 'Folders',
                description = '',
                colour = embedColour
            )
            
            for root in rootFolder:
                freePct = round((root['freeSpace'] / root['totalSpace'] * 100), 2)
                if freePct < 10:
                    embedColour = discord.Colour.red()
                diskEmbed.add_field(name='Path', value=root['path'], inline=True)
                diskEmbed.add_field(name='Free Space', value=str(freePct) + '%', inline=True)

            await ctx.send(embed=diskEmbed)

        elif mediaType == 'movie':
            await ctx.send('Radarr movies not implemented yet')
        else:
            await ctx.send('Incorrect media type `getRoot <movie|series>`\n')

    @commands.command()
    async def search(self, ctx, mediaType, *args):
        """Lookup a series based on a search term"""
        if len(args) < 1:
            await ctx.send('search requires `search <movie|series> <"the title"|tvdb-id>`\n')
        elif mediaType == 'series':
            term = "%20".join(args)

            lookup = sonarr.lookup_series(term)

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

    @commands.command()
    async def add(self, ctx, *args):
        argCount = len(args)
        if argCount < 3 > 3:
            await ctx.send('Incorrect no of arguments: `add <movie|series> <search-id> <quality-id>`\n')
            return

        mediaType = args[0]
        mediaId = args[1]
        qualityId = args[2]

        if not mediaId:
            await ctx.send('a tmdb/tvdb id is required\n `<movie|series> <id> <quality-id>`')
            return

        if not qualityId:
            await ctx.send('a quality profile id is required\n `<movie|series> <id> <quality-id>`')
            return

        if mediaType == 'series':
            series_json = sonarr.construct_series_json(mediaId, qualityId)
            addSeries = sonarr.add_series(series_json)
            if isinstance(addSeries, list):
                for item in addSeries: 
                    if item['propertyName'] == 'TvdbId':
                        await ctx.send(item['errorMessage'])

            else:
                embed = discord.Embed(
                    colour = discord.Colour.green()
                )
                
                embed.add_field(name='Year', value=addSeries['year'], inline=True)
                embed.add_field(name='Seasons', value=addSeries['seasonCount'], inline=True)
                embed.add_field(name='Status', value=addSeries['status'], inline=True)
                embed.add_field(name='Network', value=addSeries['network'], inline=True)
                embed.add_field(name='Overview', value=addSeries['overview'], inline=False)
                
                embed.set_thumbnail(url=f'https://artworks.thetvdb.com/banners/posters/{mediaId}-1.jpg')
                embed.set_author(name=f'Added: {addSeries["title"]}')

                await ctx.send(embed=embed)

        elif mediaType == 'movies':
            await ctx.send('Radarr movies not implemented yet')
            return
        else:
            await ctx.send('add requires `<movie|series>`\n')
            return

    @commands.command()
    async def quality(self, ctx, *args):
        """Get the quality profiles"""
        argCount = len(args)
        if argCount < 1:
            await ctx.send('Missing Argument: quality requires `quality <movie|series>`\n')
            return
        mediaType = args[0]

        if mediaType == 'series': 
            profiles = sonarr.get_quality_profiles()
            profileCount = len(profiles)

            if profileCount < 1:
                formattedResults = "No records were returned for that search.\n"
            else:
                formattedResults = "Here are your quality profiles:\n"
                for profile in profiles:
                    formattedResults += "- `" + str(profile['id']) + "` - " + profile['name'] + "\n"

            await ctx.send(formattedResults)

        elif mediaType == 'movie':
            await ctx.send('Radarr movies not implemented yet')
            return
        else:
            await ctx.send('quality requires `quality <movie|series>`\n')
            return

def setup(bot):
    bot.add_cog(arrCommands(bot))
    print('arrCommands is loaded')
