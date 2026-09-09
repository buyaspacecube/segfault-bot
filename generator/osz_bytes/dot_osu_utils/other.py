from generator.osz_bytes.dot_osu_utils.enums import Gamemode
from hexadecimal.int_to_hex_string import int_to_hex_string

def is_mode_taiko(dot_osu_line: str) -> bool:

    k, _, mode_str = dot_osu_line.partition(':')
    return int(mode_str) == Gamemode.TAIKO

def append_seed_to_diffname(dot_osu_line: str, seed: int) -> str:

    line_str = dot_osu_line.strip()
    seed_str = int_to_hex_string(seed)

    return f"{line_str} {seed_str}\n"

