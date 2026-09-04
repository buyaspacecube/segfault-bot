from discord import slash_command, SlashCommandGroup
from discord.ext.commands import Cog

from interface.options import get_slot_option, get_diffs_option, get_seed_option
from utils.discord_utils import get_generated_seeds_message
from utils.RNG_utils import generate_seeds
from generator.generate import generate

slot_option, diffs_option, seed_option = get_slot_option(), get_diffs_option(), get_seed_option()

class Generate(Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="generate", description="Generate a seed of the given slot")
    async def command_generate(self, ctx,
                               slot: slot_option):

        seeds = generate_seeds(1)

        message: str = get_generated_seeds_message(seeds)
        osz: File = generate(slot, seeds)
        
        await ctx.respond(message, file=osz)

    practice = SlashCommandGroup(name="practice")

    @practice.command(name="diffs", description="Generate a number of seeds without anyone else seeing")
    async def command_practice_diffs(self, ctx,
                             slot: slot_option,
                             diffs: diffs_option):

        seeds = generate_seeds(diffs)

        message: str = get_generated_seeds_message(seeds)
        osz: File = generate(slot, seeds)
        
        await ctx.respond(message, file=osz, ephemeral=True)

    @practice.command(name="seed", description="Generate a specific seed without anyone else seeing")
    async def command_practice_seed(self, ctx,
                            slot: slot_option,
                            seed: seed_option):

        seed_hex = int(seed, 16)
        seeds = [seed_hex]

        message: str = get_generated_seeds_message(seeds)
        osz: File = generate(slot, seeds)
        
        await ctx.respond(message, file=osz, ephemeral=True)

# add to bot
def setup(bot):

    generate = Generate(bot)
    bot.add_cog(generate)

