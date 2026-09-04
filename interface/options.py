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
        description = "The number of seeds to generate"
    )

def get_seed_option() -> Option:

    return Option(
        str,
        name = "seed",
        description = "The seed to generate (hexadecimal from 0000 to FFFF)"
    )

def get_player_option(number: int) -> Option:

    if number != 1 and number != 2:
        raise ValueError("Player number must be 1 or 2")

    return Option(
        Member,
        name = f"player{number}",
        description = f"The Discord username of player {number}"
    )

def get_streamer_option() -> Option:

    return Option(
        Member,
        name = "streamer",
        description = "The Discord username of the streamer"
    )
