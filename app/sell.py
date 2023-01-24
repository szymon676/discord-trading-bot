import redis 
import yfinance as yf
import discord
import math
from discord.ext import commands
from discord import app_commands

client = commands.Bot(command_prefix="!",intents=discord.Intents.all())


r = redis.Redis(host='localhost', port=6379, db=0)

@client.tree.command(name="sell_q",description="sell your quant")
async def sell_q(interaction: discord.Interaction,quantity):
    
    qnt_data = yf.download(tickers='QNT-USD', period='10m', interval='15m')
    info_raw = str(qnt_data).split()
    price = float(info_raw[11])

    user = interaction.user.id

    if r.hget(user) == None :

        await interaction.response.send_message("first you need to buy quant")

    elif quantity > r.hget(user,"quant"):
        await interaction.response.send_message("you don't have enough quant")

    elif float(r.hget(user,"quant")) > 0:
        
        
        cash = quantity * price 

        r.hincrby(user,"quant",-quantity)
        r.hincrby(user,"money",cash)

        await interaction.response.send_message("you sold " + str(quantity) + "quant")
        await interaction.response.send_message("now you have " + str(r.hget(user,"money") + "$"))