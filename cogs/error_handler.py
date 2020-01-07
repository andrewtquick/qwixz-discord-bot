import discord
from discord.ext import commands
from discord.ext.commands import BadArgument, MissingRequiredArgument

class ErrorHandler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, BadArgument):
            await ctx.send(f'{ctx.author.mention} -> **`### ERROR ###`** : Unable to find a user by that name.')
        elif isinstance(error, MissingRequiredArgument):
            await ctx.send(f'{ctx.author.mention} -> **`### ERROR ###`** : Missing required argument.')


def setup(bot):
    bot.add_cog(ErrorHandler(bot))
