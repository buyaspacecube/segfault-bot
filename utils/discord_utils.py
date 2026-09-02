from discord import Option

from repository.getters import get_slots
from utils.hex_utils import int_to_hex_string

def get_slot_option() -> Option:

    return Option(
        input_type = str,
        name = "slot",
        description = "The slot to generate",
        choices = get_slots()
    )

def get_generated_seeds_message(seeds: list[int]) -> str:

    str_seeds = [int_to_hex_string(seed) for seed in seeds]
    s = "s" if len(seeds) > 1 else ""

    return f"Generated seed{s} **{', '.join(str_seeds)}**"
