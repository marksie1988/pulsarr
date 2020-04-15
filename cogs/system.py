
import discord, yaml
from discord.ext import commands

with open("config.yml", "r") as ymlfile:
    try:
        config = yaml.safe_load(ymlfile)
    except yaml.YAMLError as exc:
        print(exc)

BOT_NAME = config['botName']

class System(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{BOT_NAME} is ready.')

    @commands.command()
    async def clear(self, ctx, amount=0):
        if amount == 0:
            await ctx.channel.purge()
        else:
            await ctx.channel.purge(limit=amount)

def setup(bot):
    bot.add_cog(System(bot))
