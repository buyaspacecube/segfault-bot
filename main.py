from discord import Bot

from dotenv import load_dotenv
from os import getenv

bot = Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is alive")

bot.load_extension('interface.generate')

load_dotenv()
token = getenv('TOKEN')
bot.run(token)
