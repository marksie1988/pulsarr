import discord, asyncio, datetime
from discord.ext import commands

class HelpCog(commands.Cog, name='Help'):
    """Formats Help Output"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, *cog):
        """Get all cogs and commands"""
        if not cog:
            embed = discord.Embed()
            cogs_desc = ''
            for x in self.bot.cogs:
                cogs_desc += ('**{}** - {}\n'.format(x,self.bot.cogs[x].__doc__)+'\n')
            embed.add_field(name='Cogs', value=cogs_desc[0:len(cogs_desc)-1],inline=False)
            await ctx.message.add_reaction(emoji='✉')
            await ctx.send(embed=embed)
        else:
            if len(cog) > 1:
                embed = discord.Embed(
                    title = 'Error!',
                    description = 'Too many cogs!'
                )
                await ctx.message.author.send('',embed=embed)
            else:
                found = False
                for x in self.bot.cogs:
                    for y in cog:
                        if x == y:
                            embed = discord.Embed()
                            scog_info = ''
                            for c in self.bot.get_cog(y).get_commands():
                                if not c.hidden:
                                    scog_info += f'**{c.name}** - {c.help}\n'
                            embed.add_field(name = f'{cog[0]} Module - {self.bot.cogs[cog[0]].__doc__}', value = scog_info)
                            found = True
            if not found:
                for x in self.bot.cogs:
                    for c in self.bot.get_cog(x).get_commands():
                        if c.name == cog[0]:
                            embed = discord.Embed()
                            embed.add_field(name = f'{c.name} - {c.help}', value = f'Proper Syntax:\n`{c.qualified_name} {c.signature}`')
                    found = True
                if not found: 
                    embed = discord.Embed(
                        title = 'Error',
                        description = 'That is not a cog'
                    )
            else:
                await ctx.message.add_reaction(emoji='✉')
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(HelpCog(bot))
    print('Help is loaded')