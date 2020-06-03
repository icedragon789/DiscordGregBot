import discord
import datetime
import praw
import random
from datetime import datetime
from discord.ext import commands

class Commands(commands.Cog):

    def __init__(self,client):
        self.client = client

    #Commands
    @commands.command(pass_context = True, aliases=['time','date','ping'])
    async def dt(self,ctx):
        now = datetime.now()
        date = now.strftime("%m/%d/%Y")
        time = now.strftime("%H:%M:%S")

        await ctx.send("Tonight's date is: {0} and the time is {1}".format(date,time))

    @commands.command()
    async def meme(self,ctx, subreddit):
        reddit = praw.Reddit(client_id="",
            client_secret="",
            user_agent="")
        memes_submissions = reddit.subreddit(subreddit).hot()
        post_to_pick = random.randint(1,10)
        for i in range(0,post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
        await ctx.send(submission.url)

def setup(client):
    client.add_cog(Commands(client))
