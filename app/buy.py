import redis
import yfinance as yf
import discord
import math
from discord import app_commands
from discord.ext import commands

r = redis.Redis(host='localhost', port=6379, db=0)

client = commands.Bot(command_prefix="!",intents=discord.Intents.all())



@client.tree.command(name="buy_q",description="buy quant")
async def buy_q(interaction: discord.Interaction,cash:int):
    
    qnt_data = yf.download(tickers='QNT-USD', period='10m', interval='15m')
    info_raw = str(qnt_data).split()
    price = float(info_raw[11])
   
    user = interaction.user.id
    
    qnt = cash / price

    if r.hget(user) == None:

        r.hset(user,"quant",qnt,"money",500-cash)
        await interaction.response.send_message("you bought " + str(qnt))
        await interaction.response.send_message("now you have " + str(r.hget(user,"money") + "$"))
        

    elif float(r.hget(user,"money")) == 0 :

        await interaction.response.send_message("you don't have enough money")


    elif float(r.hget(user,"money")) > 0:
    
        r.hincrby(user,"quant",qnt)
        r.hincrby(user,"money",-cash)

        await interaction.response.send_message("you bought " + str(qnt))
        await interaction.response.send_message("now you have " + str(r.hget(user,"money") + "$"))

        





   
    #if r.get(user) == None: 
#
    #    r.set(user,500)
    #    money = float(r.get(user))
    #    qnt = money/price
#
    #    r.set(user,qnt)
#
    #elif float(r.get(user)) > 30:
#
    #    money = float(r.get(user))
    # 
    #    qnt = money / price
    #    r.set(user,qnt)
#
    #    await interaction.response.send_message("you bought " + str(qnt) + " Qnt" )
    #elif float(r.get(user)) < 30 :
        #await interaction.response.send_message("first you need to sell your Qnt")