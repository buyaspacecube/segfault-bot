from discord import File

from generator.pack_bytes.generate_pack_bytes import generate_pack_bytes

def generate_pack(slots: list[str], seed_lists: list[list[int]], osu_only: bool = False) -> File:

    pack_bytes = generate_pack_bytes(slots, seeds, osu_only)
    return File(pack_bytes, filename="pack.zip")
