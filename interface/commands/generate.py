from discord import slash_command, SlashCommandGroup
from discord.ext.commands import Cog, guild_only

from interface.options import get_slot_option, get_diffs_option, get_seed_option
from interface.permissions import get_base_permissions, get_referee_permissions
from interface.strings import get_generated_seeds_message

from generator.seeds import get_match_seeds, get_random_seeds
from generator.generate_osz import generate_osz

slot_option, diffs_option, seed_option = get_slot_option(), get_diffs_option(), get_seed_option()

base_permissions = get_base_permissions()
referee_permissions = get_referee_permissions()

def seed_str_to_hex(seed: str) -> int:

    seed_hex = int(seed, 16)

    if seed_hex < 0 or seed_hex > (2**16 - 1):
        raise ValueError("Seed must be hexadecimal 0000-FFFF")

    return seed_hex

async def generate_and_send(ctx, slot: str, seeds: list[int], ephemeral: bool = False):

    osz: File = generate_osz(slot, seeds)
    message: str = get_generated_seeds_message(seeds)

    await ctx.respond(message, file=osz, ephemeral=ephemeral)

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
    @guild_only()
    async def command_generate(self, ctx,
                               slot: slot_option):

        match_ID = ctx.channel.id
        all_seeds = get_match_seeds(match_ID)

        seed = all_seeds[slot]
        seeds = [seed]

        await generate_and_send(ctx, slot, seeds)

    #
    # practice commands
    #
    practice = SlashCommandGroup(name="practice", default_member_permissions = base_permissions)

    @practice.command(
        name="diffs",
        description="Generate a number of seeds without anyone else seeing"
    )
    @guild_only()
    async def command_practice_diffs(self, ctx,
                             slot: slot_option,
                             diffs: diffs_option):

        seeds = get_random_seeds(diffs)

        await generate_and_send(ctx, slot, seeds, ephemeral=True)

    @practice.command(
        name="seed",
        description="Generate a specific seed without anyone else seeing"
    )
    @guild_only()
    async def command_practice_seed(self, ctx,
                            slot: slot_option,
                            seed: seed_option):

        seed_hex = seed_str_to_hex(seed)
        seeds = [seed_hex]

        await generate_and_send(ctx, slot, seeds, ephemeral=True)

# add to bot
def setup(bot):

    generate = Generate(bot)
    bot.add_cog(generate)

