import discord
from datetime import datetime
from discord.ext import commands
from discord.ext.commands import command as Command
from discord.ext.commands import Context, Cog

class AdminCog(Cog):

    def __init__(self, bot):
        self.bot = bot

    @Command(name='userid', help='Returns users id, usage: !userid <user>')
    async def get_userid(self, ctx: Context, member: discord.User):
        await ctx.channel.send(f"{ctx.author.mention} -> {member.name}'s user id is: `{member.id}`")

    @Command(name='kick', help='Kicks users, usage: !kick <username or user id> <reason>')
    @commands.has_role('Admin')
    async def kick_user(self, ctx: Context, member: discord.User, *reason: str):
        curr_time = datetime.now()
        format_reason = ' '.join(reason)
        embed = discord.Embed(title='')
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name='**User**', value=member.name)
        embed.add_field(name='**User ID**', value=member.id, inline=False)
        embed.add_field(name='**Reason**', value=format_reason, inline=False)
        embed.add_field(name='**Timestamp**', value=f'{curr_time.strftime("%b %d %Y %I:%M %p")}', inline=False)
        await ctx.send(f'**Kick user initiated by {ctx.author.mention}**', embed=embed)

    @Command(name='ban', help='Bans user, !ban <member or member id> <reason>')
    @commands.has_role('Admin')
    async def ban_user(self, ctx: Context, member: discord.User, *reason: str):
        curr_time = datetime.now()
        format_reason = ' '.join(reason)
        embed = discord.Embed(title='')
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name='**User**', value=member.name)
        embed.add_field(name='**User ID**', value=member.id, inline=False)
        embed.add_field(name='**Reason**', value=format_reason, inline=False)
        embed.add_field(name='**Timestamp**', value=f'{curr_time.strftime("%b %d %Y %I:%M %p")}', inline=False)
        await ctx.send(f'**Ban user initiated by {ctx.author.mention}**', embed=embed)

    @Command(name='addrole', help='Add role to user, !addrole <member or member id> <role>')
    async def add_user_role(self, ctx: Context, member: discord.Client, *role: discord.Role):
        await member.add_roles(role)
        await ctx.send(f'{ctx.author.mention} -> **`### SUCCESS ###`** : {member.name} has been granted {role}')

    async def remove_user_role(self, ctx: Context):
        pass

    @Command(name='roles', help='Display roles, !roles')
    @commands.has_role('Admin')
    async def list_roles(self, ctx: Context):

        roles = ', '

        # await ctx.send(f'Current roles are {ctx.guild.roles}')

    async def add_guild_role(self, ctx: Context):
        pass

    async def rem_guild_role(self, ctx: Context):
        pass

    async def add_user_perm(self, ctx: Context):
        pass

    async def rem_user_perm(self, ctx: Context):
        pass

    async def check_user_perm(self, ctx: Context):
        pass

    async def add_text_channel(self, ctx: Context):
        pass

    async def rem_text_channel(self, ctx: Context):
        pass

    async def add_voice_channel(self, ctx: Context):
        pass

    async def change_nick(self, ctx: Context):
        pass

    async def add_cmd(self, ctx: Context):
        pass

    async def del_msg(self, ctx: Context):
        pass


def setup(bot):
    bot.add_cog(AdminCog(bot))

