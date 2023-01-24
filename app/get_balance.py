import discord 
import redis
import math
from discord.ext import commands
from discord import app_commands


r = redis.Redis(host='localhost', port=6379, db=0)

client = commands.Bot(command_prefix="!",intents=discord.Intents.all())

@client.tree.command(name="get_balance",description="get your current balance")
async def get_balance(interaction:discord.Interaction):

    user = interaction.user.id
    money = float(r.hget(user,"money"))
    qnt = float(r.hget(user,"quant"))

    await interaction.response.send_message(f"now you have {str(money)}$ and {str(qnt)} qnt ")  
    
    if r.hget(user) == None:
        await interaction.response.send_message("your account is clear")