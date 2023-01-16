import redis 
import yfinance as yf
import discord
from discord.ext import commands
from discord import app_commands

client = commands.Bot(command_prefix="!",intents=discord.Intents.all())


r = redis.Redis(host='localhost', port=6379, db=0)

@client.tree.command(name="sell_q",description="sell your quant")
async def sell_q(interaction: discord.Interaction):
    
    qnt_data = yf.download(tickers='QNT-USD', period='10m', interval='15m')
    info_raw = str(qnt_data).split()
    price = float(info_raw[11])

    user = interaction.user.id

    if r.get(user) == None or float(r.get(user)) > 30 :

        await interaction.response.send_message("you haven't bought anything yet")

    elif float(r.get(user)) < 30:

        qnt = float(r.get(user))

        money = qnt * price

        r.set(user,money)
        await interaction.response.send_message("your current balance is " + str(money) + "$")
