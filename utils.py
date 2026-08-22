from discord import Option

from repository.utils import get_slots

def get_slot_option() -> Option:

    return Option(
        input_type = str,
        name = "slot",
        description = "The slot to generate",
        choices = get_slots()
    )
