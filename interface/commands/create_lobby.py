from discord import slash_command, SlashCommandGroup, Member, Message, File
from discord.ext.commands import Cog

from generator.seeds import get_match_seeds
from generator.generate_pack import generate_pack
from interface.options import get_player_option, get_streamer_option, get_lobby_ID_option
from interface.permissions import get_referee_permissions
from hexadecimal.int_to_hex_string import int_to_hex_string

#
# create thread
#
async def create_thread(ctx, title: str, is_match: bool, players: list[Member], **staff) -> Message:
    
    player_mentions = [p.mention for p in players]
    staff_mentions: list[str] = list()

    for role, member in staff.items():

        if type(member) != Member:
            raise TypeError("Input is not discord user")

        staff_mentions.append(f"{member.mention} will be your {role}")

    player_string = ' '.join(player_mentions)
    staff_string = '\n'.join(staff_mentions)

    match_or_lobby = "match" if is_match else "lobby"

    interaction = await ctx.respond(f"""
{player_string} your {match_or_lobby} is starting soon!

{staff_string}
    """)

    message = await interaction.original_response()
    await message.create_thread(name=title)
    
    return message

#
# DM stuff to people
#
async def send_seeds_to_referee(ctx, title: str, seeds: list[int], referee: Member):

    hex_seeds = [int_to_hex_string(s) for s in seeds]
    seeds_string = '\n'.join(hex_seeds)

    await referee.send(f"""
Seeds for **{title}**
Copy these using the copy button at the top right, then paste onto the ref sheet!

```
{seeds_string}
```
    """)

async def send_pack_to_streamer(ctx, title: str, slots: list[str], seeds: list[int], streamer: Member):

    pack: File = generate_pack(slots, seeds, osu_only=True)

    await streamer.send(f"""
Generated maps for **{title}**
This includes .osu files ONLY! Make sure you already have the full mappool before downloading
After downloading, restart your stable streaming client
    """, file=pack)

#
# commands
#
class CreateLobby(Cog):

    def __init__(self, bot):
        self.bot = bot

    create = SlashCommandGroup(name="create")

    @create.command(
        name = "match",
        description = "(REFEREE ONLY) Start a Segfault Cup match",
        default_member_permissions = get_referee_permissions()
    )
    async def command_create_match(self, ctx,
                                   player1: get_player_option(1),
                                   player2: get_player_option(2),
                                   streamer: get_streamer_option()
                                   ):

        referee = ctx.author

        match_title = f"{player1.nick} vs. {player2.nick}"
        players = [player1, player2]

        thread_message = await create_thread(ctx, match_title, is_match=True, players=players, referee=referee, streamer=streamer)

        match_ID = thread_message.id
        slots_and_seeds = get_match_seeds(match_ID)
        
        slots, seeds = slots_and_seeds.keys(), slots_and_seeds.values()

        await send_seeds_to_referee(ctx, match_title, seeds, referee)
        await send_pack_to_streamer(ctx, match_title, slots, seeds, streamer)

    @create.command(
        name = "qualifiers",
        description = "(REFEREE ONLY) Start a Segfault Cup qualifiers lobby",
        default_member_permissions = get_referee_permissions()
    )
    async def command_create_qualifiers(self, ctx,
                                        lobby_ID: get_lobby_ID_option(),
                                        player1: get_player_option(1, required=True),  player2: get_player_option(2, required=False),
                                        player3: get_player_option(3, required=False), player4: get_player_option(4, required=False),
                                        player5: get_player_option(5, required=False), player6: get_player_option(6, required=False),
                                        player7: get_player_option(7, required=False), player8: get_player_option(8, required=False)
                                        ):

        referee = ctx.author

        lobby_title = f"Qualifiers lobby {lobby_ID}"

        possible_players = [player1, player2, player3, player4, player5, player6, player7, player8]
        players = [p for p in possible_players if p]

        thread_message = await create_thread(ctx, lobby_title, is_match=False, players=players, referee=referee)

        match_ID = thread_message.id
        slots_and_seeds = get_match_seeds(match_ID)
        
        seeds = slots_and_seeds.values()
        await send_seeds_to_referee(ctx, lobby_title, seeds, referee)
        
# add to bot
def setup(bot):

    create_lobby = CreateLobby(bot)
    bot.add_cog(create_lobby)
