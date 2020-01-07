import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

extensions = [
    'cogs.events',
    'cogs.admin',
    'cogs.main',
    'cogs.load',
    'cogs.error_handler']



if __name__ == '__main__':

    for extension in extensions:
        bot.load_extension(extension)

    TOKEN = open('.token', 'r').read()
    bot.run(TOKEN)
