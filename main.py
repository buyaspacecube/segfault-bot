from discord import Bot

from dotenv import load_dotenv
from os import getenv

from datetime import datetime

bot = Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is alive")

@bot.listen
async def on_application_command(ctx):

    timestamp = datetime.now()
    user = ctx.author.name
    command = ctx.command.qualified_name

    option_strings = [f"{o['name']}:{o['value']}" for o in ctx.selected_options]
    options = ' '.join(option_strings)

    print(f"[{timestamp}] {user} used /{command} {options}")

bot.load_extension('interface.commands.generate')
bot.load_extension('interface.commands.create_lobby')
bot.load_extension('interface.commands.publish_mappool')

load_dotenv()
token = getenv('TOKEN')
bot.run(token)
