from discord import Option
from repository.getters import get_slots

def get_slot_option() -> Option:

    return Option(
        input_type = str,
        name = "slot",
        description = "The slot to generate",
        choices = get_slots()
    )

def get_diffs_option() -> Option:

    return Option(
        input_type = int,
        name = "diffs",
        description = "The number of seeds to generate"
    )

def get_seed_option() -> Option:

    return Option(
        input_type = str,
        name = "seed",
        description = "The seed to generate (hexadecimal from 0000 to FFFF)"
    )
