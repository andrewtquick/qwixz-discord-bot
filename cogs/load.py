import discord
from discord.ext import commands

class CogControl(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def reload_cog(self, ctx, *, cog: str):

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as err:
            await ctx.send(f'**`ERROR`**: {type(err).__name__} - {err}')
        else:
            await ctx.send(f'**`SUCCESS`**')

def setup(bot):
    bot.add_cog(CogControl(bot))
