import discord
import datetime
from discord.ext import commands


class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='embeds')
    @commands.guild_only()
    async def example_embed(self, ctx):
        """A simple command which showcases the use of embeds.
        Have a play around and visit the Visualizer."""

        embed = discord.Embed(title='Kicked User')
        embed.add_field(name='Member Name', value=member.name)
        embed.add_field(name='Member ID', value=member.id)
        embed.set_footer(text=f'Kick initialed on {datetime.datetime.utcfromtimestamp(1578354719)}')

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(MainCog(bot))
