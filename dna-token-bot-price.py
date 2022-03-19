import requests, json
import discord
from discord.ext import commands, tasks
from pythonpancakes import PancakeSwapAPI

TOKEN = "DNA-BOT-TOKEN-HERE"

ps = PancakeSwapAPI()

client = discord.Client()

@client.event
async def on_ready():
    dna_price.start()


@tasks.loop(seconds=60)
async def dna_price():
    dna_token = ps.tokens("0x444ddc9ab6e938511fdd56f89ec334d38cadee0f")
    url = requests.get("http://www.floatrates.com/daily/usd.json")
    data = url.json()
    usd_php = data["php"]["rate"]
    current_price = round(float(round(float(dna_token["data"]["price"]),2) * usd_php),2)

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name="₱ {}".format(current_price)))

client.run(TOKEN)