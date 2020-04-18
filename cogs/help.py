import discord, yaml, requests
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def help(ctx):
        author = ctx.message.author

        embed = discord.Embed(
            color = discord.Colour.orange()
        )

        embed.set_author(name='Help')
        embed.set_field(name='search', value='Search for movie or show `search <movie|show> <"title"|tvdb>`')

        await bot.send_message(author, embed=embed)
        
def setup(bot):
    bot.add_cog(Help(bot))
