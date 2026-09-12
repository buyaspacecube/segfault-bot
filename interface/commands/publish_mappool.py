from discord import slash_command, SlashCommandGroup
from discord.ext.commands import Cog

from interface.permissions import get_admin_permissions
from interface.options import get_practice_pack_option
from interface.strings import get_mappool_messages
from generator.seeds import get_practice_seeds
from generator.pack_bytes.generate_pack_bytes import generate_pack_bytes
from repository.getters import get_slots

async def generate_practice_pack(ctx):

    slots = get_slots()
    seed_lists = [get_practice_seeds() for s in slots]
    
    pack_bytes = generate_pack_bytes(slots, seed_lists)

    with open("pack.zip", mode='wb') as f:

        data = pack_bytes.getvalue()
        f.write(data)

    await ctx.respond("Practice pack written to disk", ephemeral=True)

async def send_mappool_message(ctx, practice_pack: str):

    for message in get_mappool_messages(practice_pack):
        await ctx.send(message)

    await ctx.respond("Done", ephemeral=True)

class PracticePack(Cog):

    def __init__(self, bot):
        self.bot = bot

    publish = SlashCommandGroup(name="publish")

    @publish.command(
        name="mappool",
        description="(ADMIN ONLY) Publish the mappool including practice pack",
        default_member_permissions = get_admin_permissions()
    )
    async def command_publish_mappool(self, ctx,
                                      practice_pack = get_practice_pack_option()
                                      ):

        if practice_pack:
            await send_mappool_message(ctx, practice_pack)

        else:
            await generate_practice_pack(ctx)

# add to bot
def setup(bot):

    practice_pack = PracticePack(bot)
    bot.add_cog(practice_pack)
