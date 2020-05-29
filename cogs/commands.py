import discord
import datetime
from discord.ext import commands

class Commands(commands.Cog):

    def __init__(self,client):
        self.client = client

    #Events
    # @commands.Cog.listener()
    # async def on_ready(self):
    #     await client.change_presence(status=discord.Status.idle, activity=discord.Game('Operating Systems'))
    #     print('Bot is online')

    #Commands
    @commands.command(pass_context = True, aliases=['time','date','ping'])
    async def dt(self,ctx):
        data = datetime.datetime.now()
        await ctx.send('Tonight is: {}'.format(data))


def setup(client):
    client.add_cog(Commands(client))
