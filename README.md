import discord
from discord.ext import commands
from token import token

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def merhaba():
    print(f'merhaba ben temizlik botuyum çevre temizliği çok önemli')

@bot.command()
async def kirli(ctx):
    await ctx.send(f'fabrika bacalarına filtre takılması lazım')

@bot.command()
async def temiz(ctx):
    await ctx.send(f'mükemmel')

bot.run(token)
