from discord import slash_command, SlashCommandGroup
from discord.ext.commands import Cog

from interface.options import get_slot_option, get_diffs_option, get_seed_option
from interface.permissions import get_referee_permissions
from interface.messages import get_generated_seeds_message

from generator.seeds import get_match_seeds, get_random_seeds
from generator.generate_osz import generate_osz

slot_option, diffs_option, seed_option = get_slot_option(), get_diffs_option(), get_seed_option()
referee_permissions = get_referee_permissions()

class Generate(Cog):

    def __init__(self, bot):
        self.bot = bot

    #
    # generate (for matches only)
    #
    @slash_command(
        name="generate",
        description="(REFEREE ONLY) Generate a seed of the given slot to be played in match",
        default_member_permissions = referee_permissions
    )
    async def command_generate(self, ctx,
                               slot: slot_option):

        match_ID = ctx.channel.id
        all_seeds = get_match_seeds(match_ID)

        seed = all_seeds[slot]
        seeds = [seed]

        message: str = get_generated_seeds_message(seeds)
        osz: File = generate_osz(slot, seeds)
        
        await ctx.respond(message, file=osz)

    #
    # practice commands
    #
    practice = SlashCommandGroup(name="practice")

    @practice.command(
        name="diffs",
        description="Generate a number of seeds without anyone else seeing"
    )
    async def command_practice_diffs(self, ctx,
                             slot: slot_option,
                             diffs: diffs_option):

        seeds = get_random_seeds(diffs)

        message: str = get_generated_seeds_message(seeds)
        osz: File = generate_osz(slot, seeds)
        
        await ctx.respond(message, file=osz, ephemeral=True)

    @practice.command(
        name="seed",
        description="Generate a specific seed without anyone else seeing"
    )
    async def command_practice_seed(self, ctx,
                            slot: slot_option,
                            seed: seed_option):

        seed_hex = int(seed, 16)
        seeds = [seed_hex]

        message: str = get_generated_seeds_message(seeds)
        osz: File = generate_osz(slot, seeds)
        
        await ctx.respond(message, file=osz, ephemeral=True)

# add to bot
def setup(bot):

    generate = Generate(bot)
    bot.add_cog(generate)

