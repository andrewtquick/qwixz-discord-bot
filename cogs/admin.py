from discord.ext import commands

class AdminCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='addchan')
    @commands.has_role('Admin')
    async def add_channel(self, name, chantype='text'):
        # await self.bot.create_channel(name, chantype)



def setup(bot):
    bot.add_cog(AdminCog(bot))

