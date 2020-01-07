import discord
from datetime import datetime
from discord.ext import commands

class AdminCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='userid', help='Returns users id, usage: !userid <user>')
    async def get_userid(self, ctx, member: discord.User):
        await ctx.channel.send(f"{ctx.author.mention} -> {member.name}'s user id is: `{member.id}`")

    @commands.command(name='kick', help='Kicks users, usage: !kick <username or user id> <reason>')
    @commands.has_role('Admin')
    async def kick_user(self, ctx, member: discord.User, *reason: str):

        # if reason == ():
        #     await ctx.send(f'{ctx.author.mention} Please include a reason for the kick. !kick <user> <reason>')
        # else:
        curr_time = datetime.now()
        format_reason = ' '.join(reason)
        embed = discord.Embed(title='')
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name='**User**', value=member.name)
        embed.add_field(name='**User ID**', value=member.id, inline=False)
        embed.add_field(name='**Reason**', value=format_reason, inline=False)
        embed.add_field(name='**Timestamp**', value=f'{curr_time.strftime("%b %d %Y %I:%M %p")}', inline=True)
        await ctx.send(f'**Kick user initiated by {ctx.author.mention}**', embed=embed)

    @commands.command(name='ban', help='Bans user, !ban <member or member id> <reason>')
    @commands.has_role('Admin')
    async def ban_user(self, ctx, member: discord.User, *reason: str):

        if reason == ():
            await ctx.send(f'{ctx.author.mention} Please include a reason for the kick. !ban <user> <reason>')
        else:
            curr_time = datetime.now()
            format_reason = ' '.join(reason)
            embed = discord.Embed(title='')
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name='**User**', value=member.name)
            embed.add_field(name='**User ID**', value=member.id, inline=False)
            embed.add_field(name='**Reason**', value=format_reason, inline=False)
            embed.add_field(name='**Timestamp**', value=f'{curr_time.strftime("%b %d %Y %I:%M %p")}', inline=False)
            await ctx.send(f'**Ban user initiated by {ctx.author.mention}**', embed=embed)

def setup(bot):
    bot.add_cog(AdminCog(bot))

