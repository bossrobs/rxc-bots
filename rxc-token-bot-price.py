import requests, json
import discord
from discord.ext import commands, tasks

TOKEN = "RXC-BOT-TOKEN-HERE"

client = discord.Client()

@client.event
async def on_ready():
    rxc_price.start()

@tasks.loop(seconds=60)
async def rxc_price():
        url = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ran-x-crypto&vs_currencies=php&include_24hr_change=true")
        data = url.json()
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name="₱"+ format(round(data['ran-x-crypto']['php'],2)) +"@"+ format(round(data['ran-x-crypto']['php_24h_change'],2))+"%"))

client.run(TOKEN)