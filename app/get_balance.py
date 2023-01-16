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
    balance  = float(r.get(user))
    if math.ceil(float(r.get(user))) < 20:
        await interaction.response.send_message("your Qnt is " +str(balance)) 
    elif math.ceil(float(r.get(user))) > 20:
        await interaction.response.send_message("your balance is " + str(balance))
    else:
        await interaction.response.send_message("you haven't bought anything yet")