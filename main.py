import os
import discord
from discord.ext import commands
import random

# https://discord.gg/5NpaKT8

class QwixzBot(discord.Client):

    bot = commands.Bot(command_prefix='!')

    async def on_ready(self):
        print(f'{self.user} has logged in.')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.lower() == 'test':
            await message.channel.send('Testing what?')

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(f'{member.name}, Welcome to Qwixz dev discord server.')

    @bot.command(name='ping', help='Replies with "Pong!"')
    async def ping(self, ctx):
        await ctx.send('Pong!')


if __name__ == '__main__':

    DISCORD_TOKEN = open('.token', 'r').read()
    client = QwixzBot()
    client.run(DISCORD_TOKEN)