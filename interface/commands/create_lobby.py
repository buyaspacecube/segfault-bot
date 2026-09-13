from discord import slash_command, SlashCommandGroup, Member, Message, File
from discord.ext.commands import Cog

from interface.strings import get_lobby_created_message, get_referee_seeds_message, get_streamer_pack_message, int_to_hex_string
from interface.options import get_player_option, get_streamer_option, get_lobby_ID_option
from interface.permissions import get_referee_permissions

from generator.seeds import get_match_seeds
from generator.generate_pack import generate_pack

referee_permissions = get_referee_permissions()

async def create_thread(ctx, title: str, is_match: bool, players: list[Member], **staff) -> Message:

    staff_dict: dict = dict()

    for role, member in staff.items():

        if type(member) != Member:
            raise TypeError("Input is not discord user")

        staff_dict[role] = member

    lobby_created_message = get_lobby_created_message(players, staff_dict, is_match)
    interaction = await ctx.respond(lobby_created_message)

    message = await interaction.original_response()
    await message.create_thread(name=title)
    
    return message

async def send_seeds_to_referee(ctx, title: str, seeds: list[int], referee: Member):

    referee_seeds_message = get_referee_seeds_message(title, seeds)
    await referee.send(referee_seeds_message)

async def send_pack_to_streamer(ctx, title: str, slots: list[str], seeds: list[int], streamer: Member):

    pack: File = generate_pack(slots, seeds, osu_only=True)
    streamer_pack_message = get_streamer_pack_message(title)

    await streamer.send(streamer_pack_message, file=pack)

class CreateLobby(Cog):

    def __init__(self, bot):
        self.bot = bot

    create = SlashCommandGroup(name="create", default_member_permissions = referee_permissions)

    @create.command(
        name = "match",
        description = "(REFEREE ONLY) Start a Segfault Cup match"
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
        
        seed_lists = [
            [s] for s in seeds
        ]

        await send_seeds_to_referee(ctx, match_title, seeds, referee)
        await send_pack_to_streamer(ctx, match_title, slots, seed_lists, streamer)

    @create.command(
        name = "qualifiers",
        description = "(REFEREE ONLY) Start a Segfault Cup qualifiers lobby"
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
