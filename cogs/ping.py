import discord
from discord.ext import commands
import time

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong!\n{round(self.bot.latency * 1000)}ms')

def setup(bot):
    bot.add_cog(ping(bot))