from discord.ext import commands

bot = commands.Bot(command_prefix='!')

bot.load_extension("cogs.events")
bot.load_extension("cogs.admin")
bot.load_extension("cogs.main")


if __name__ == '__main__':

    TOKEN = open('.token', 'r').read()
    bot.run(TOKEN)
