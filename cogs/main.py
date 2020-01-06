from discord.ext import commands


class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='sum', help='Sum of two numbers. Usage: !sum <int> <int>')
    async def sum_nums(self, ctx, num1, num2):

        print(ctx.content.author.rsplit('#', 1))

        # try:
        #     await ctx.channel.send(f'@{ctx.content.author.rsplit('#', 1)} the sum is: {int(num1) + int(num2)}')
        # except:
        #     await ctx.channel.send('Please try again. Proper usage: !sum <int> <int>')

def setup(bot):
    bot.add_cog(MainCog(bot))
