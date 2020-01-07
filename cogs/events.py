import discord
from discord.ext import commands
from discord.ext.commands import Context

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user} has logged in!')
        await self.bot.change_presence(activity=(discord.Game(name='Being Configured')))

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.User):
        await member.send('Welcome to the Qwixz Discord Bot development server.\nThis bot is currently being solely developed by Xylr#0781\n\nThis message will definitely change in the future.')

    @commands.Cog.listener()
    async def on_message(self, ctx: Context):
        if ctx.author == self.bot.user:
            return

        if ctx.content.lower() in ['hello', 'hi', 'sup']:
            await ctx.channel.send(f'Hello {ctx.author.mention}!')


def setup(bot):
    bot.add_cog(Events(bot))
