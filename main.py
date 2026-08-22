from discord import Bot, ApplicationContext, File

from dotenv import load_dotenv
from os import getenv

from utils import get_slot_option
from generator.generate import generate

bot = Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is alive")

slot_option = get_slot_option()

#
# generate command (for referees)
#
@bot.command(name="generate", description="Generate a difficulty of the given slot")
async def bot_generate(ctx: ApplicationContext,
                       slot: slot_option):

    osz: File = generate(slot, 1)
    await ctx.respond(file=osz)

#
# practice commands (for players)
#
practice = bot.create_group(name="practice", description="Generate difficulties without anyone else seeing")

@practice.command(name="diffs", description="Generate a number of difficulties to practice")
async def bot_practice_diffs(ctx: ApplicationContext,
                       slot: slot_option,
                       diffs: int):

    osz: File = generate(slot, diffs)
    await ctx.respond(file=osz, ephemeral=True)

@practice.command(name="seed", description="Generate a specific seed to practice")
async def bot_practice_seed(ctx: ApplicationContext,
                       slot: slot_option,
                       seed: int):

    osz: File = generate(slot, 1, seed)
    await ctx.respond(file=osz, ephemeral=True)

#
# run
#
load_dotenv()
token = getenv('TOKEN')
bot.run(token)
