from discord import slash_command, SlashCommandGroup, File
from discord.ext.commands import Cog

from generator.seeds import get_match_seeds
from generator.generate_pack import generate_pack
from interface.options import get_player_option, get_streamer_option
from interface.permissions import get_referee_permissions
from hexadecimal.int_to_hex_string import int_to_hex_string

player1_option, player2_option = get_player_option(1), get_player_option(2)
streamer_option = get_streamer_option()

referee_permissions = get_referee_permissions()

match_start_string = """
{p1} and {p2}, your match is starting soon!

{ref} will be your referee
{stream} will be your streamer
"""

referee_seeds_string = """
Seeds for **{title}**
Copy these using the copy button at the top right, then paste onto the ref sheet!

```
{seeds}
```
"""

streamer_pack_string = """
Generated maps for **{title}**
This includes .osu files ONLY! Make sure you already have the full mappool before downloading
After downloading, restart your stable streaming client
"""

class CreateThread(Cog):

    def __init__(self, bot):
        self.bot = bot

    create = SlashCommandGroup(name="create")

    @create.command(
        name = "thread",
        description = "(REFEREE ONLY) Create the thread for a Segfault Cup match",
        default_member_permissions = referee_permissions
    )
    async def command_create_thread(self, ctx,
                                    player1: player1_option,
                                    player2: player2_option,
                                    streamer: streamer_option):

        referee = ctx.author

        match_title = f"{player1.nick} vs. {player2.nick}"

        #
        # start match
        #
        match_start_string_formatted = match_start_string.format(
            p1 = player1.mention,
            p2 = player2.mention,
            ref = referee.mention,
            stream = streamer.mention
        )

        message = await ctx.send(match_start_string_formatted)
        await message.create_thread(name=match_title)

        #
        # DM seeds to referee
        #
        match_ID = message.id
        slots_and_seeds = get_match_seeds(match_ID)

        slots: list[str] = slots_and_seeds.keys()
        seeds: list[int] = slots_and_seeds.values()

        seeds_string = '\n'.join([
            int_to_hex_string(seed)
            for seed in seeds
        ])

        referee_seeds_string_formatted = referee_seeds_string.format(
            title = match_title,
            seeds = seeds_string
        )

        await referee.send(referee_seeds_string_formatted)

        #
        # DM pack to streamer
        #
        pack: File = generate_pack(slots, seeds, osu_only=True)
        
        streamer_pack_string_formatted = streamer_pack_string.format(
            title = match_title
        )

        await streamer.send(streamer_pack_string_formatted, file=pack)
        
# add to bot
def setup(bot):

    create_thread = CreateThread(bot)
    bot.add_cog(create_thread)
