from discord import File

from generator.osz_bytes.generate_osz_bytes import generate_osz_bytes
from repository.getters import get_name_for_packaged_osz

def generate_osz(slot: str, seeds: list[int]) -> File:

    osz_bytes = generate_osz_bytes(slot, seeds)
    filename = get_name_for_packaged_osz(slot)

    return File(osz_bytes, filename=filename)
