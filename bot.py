import discord
import math
from discord.ext import commands
from discord import app_commands
from config import token
from app import buy_q,sell_q,get_balance
import yfinance as yf

client = commands.Bot(command_prefix="!",intents=discord.Intents.all())



qnt_data = yf.download(tickers='QNT-USD', period='10m', interval='15m')
info_raw = str(qnt_data).split()
price = math.ceil(float(info_raw[11]))



@client.event
async def on_ready():

    await client.tree.sync()   
    await client.change_presence(status=discord.Status.idle,activity = discord.Game(name=f"Quant Price: {price}$"))
    

@client.tree.command(name="hello",description="say hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("hello")


client.tree.add_command(buy_q)
client.tree.add_command(sell_q)
client.tree.add_command(get_balance)


client.run(token)