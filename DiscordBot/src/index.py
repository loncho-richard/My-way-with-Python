import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>', description="This is a helper bot")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('MTAxODE4NTU2ODE3MTA2OTU2Mg.GuLgw6.QRptF4fusOenmbaO0xpa9Sb7IFAxn2bitpfLUc')