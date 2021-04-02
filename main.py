# https://discordpy.readthedocs.io/en/latest/quickstart.html
from discord.ext import commands
from functions.Timetable import lecturenow
from Crypto import ltp

bot = commands.Bot(command_prefix='$')

print('bot is on and running')


@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')


@bot.command()
async def test(ctx):
    await ctx.send('ok good till now')


@bot.command()
async def meme(ctx):
    await ctx.send('pls meme')


@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)


@bot.command()
async def sub(ctx, a: int, b: int):
    await ctx.send(a - b)


@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a * b)


@bot.command()
async def div(ctx, a: int, b: int):
    await ctx.send(a / b)


@bot.command()
async def who(ctx):
    ctx.message.channel.typing()
    await ctx.send(ctx.message.author.name)


@bot.command()
async def cryptoprice(ctx, arg):
    price = ltp(arg)
    await ctx.send(price)

@bot.command()
async def lec_now(ctx, enrol):
    await ctx.send(lecturenow(enrol))

bot.run('ODI3MTU3OTM2MTU3NDkxMjQw.YGW82w.oGAP_prDffYtudAntFbBaw1Pfgw')
