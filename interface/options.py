from discord import Option, Member
from repository.getters import get_slots

def get_slot_option() -> Option:

    return Option(
        str,
        name = "slot",
        description = "The slot to generate",
        choices = get_slots()
    )

def get_diffs_option() -> Option:

    return Option(
        int,
        name = "diffs",
        description = "The number of seeds to generate",
        min_value = 1, max_value = 5
    )

def get_seed_option() -> Option:

    return Option(
        str,
        name = "seed",
        description = "The seed to generate (hexadecimal from 0000 to FFFF)"
    )

def get_player_option(number: int, required: bool = True) -> Option:

    if number < 1 or number > 8:
        raise ValueError("Player number must be 1-8")

    return Option(
        Member,
        name = f"player{number}",
        description = f"The Discord username of player {number}",
        required = required
    )

def get_streamer_option() -> Option:

    return Option(
        Member,
        name = "streamer",
        description = "The Discord username of the streamer"
    )

def get_lobby_ID_option() -> Option:

    return Option(
        int,
        name = "lobby_id",
        description = "The ID of the qualifiers lobby"
    )

def get_practice_pack_option() -> Option:

    return Option(
        str,
        name = "practice_pack",
        description = "The link to the uploaded practice pack",
        required = False
    )
