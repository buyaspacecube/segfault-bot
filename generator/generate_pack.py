from discord import File

from generator.pack_bytes.generate_pack_bytes import generate_pack_bytes

def generate_pack(slots: list[str], seeds: list[int]) -> File:

    pack_bytes = generate_pack_bytes(slots, seeds)
    return File(pack_bytes, filename="pack.zip")
