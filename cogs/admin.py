import discord
from datetime import datetime
from discord.ext import commands

class AdminCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='userid')
    @commands.has_role('Admin')
    async def get_userid(self, ctx, member: discord.User):
        await ctx.channel.send(f"{ctx.author.mention} -> {member.name}'s user id is: `{member.id}`")

    @commands.command(name='kick')
    @commands.has_role('Admin')
    async def kick_user(self, ctx, member: discord.User, reason: str):
        embed = discord.Embed(title='Kicked User')
        embed.add_field(name='Member Name', value=member.name)
        embed.add_field(name='Member ID', value=member.id)
        embed.add_field(name='Reason', value=reason, inline=False)
        embed.add_field(name='Timestamp', value=f'{datetime.utcfromtimestamp(datetime.now())}', inline=True)
        embed.add_field(name='Admin', value=ctx.author.mention, inline=True)

        await ctx.send(embed=embed)
        # await ctx.channel.send(f'Kicking name:**`{member.name}`** id:`{member.id}` for **`{reason}`**')

    @commands.command(name='ban')
    @commands.has_role('Admin')
    async def ban_user(self, ctx, member: discord.User, reason: str, days: int):
        await ctx.channel.send(f'Banning **`{member.name}`** id:`{member.id}` for **`{reason}`** and deleting {days} days of previous messages.')

def setup(bot):
    bot.add_cog(AdminCog(bot))

