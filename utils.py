from discord import Option, File

from repository.utils import get_slots
from converter.utils import int_to_hex_string
from generator.generate import generate

def get_slot_option() -> Option:

    return Option(
        input_type = str,
        name = "slot",
        description = "The slot to generate",
        choices = get_slots()
    )

def get_message_and_osz(slot: str, seeds: list[int]) -> (str, File):

    str_seeds = [int_to_hex_string(seed) for seed in seeds]
    s = "s" if len(seeds) > 1 else ""
    
    message: str = f"Generated seed{s} **{', '.join(str_seeds)}**"
    osz: File = generate(slot, seeds)

    return (message, osz)
