import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user} has logged in!')
        await self.bot.change_presence(activity=(discord.Game(name='Being Configured', type='watching')))

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.content.lower() in ['hello', 'hi', 'sup']:
            await message.channel.send(f'Hello {message.author.mention}!')


def setup(bot):
    bot.add_cog(Events(bot))

