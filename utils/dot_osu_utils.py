from enum import Enum

from utils.hex_utils import int_to_hex_string

class Gamemode(int, Enum):
    OSU = 0
    TAIKO = 1
    CATCH = 2
    MANIA = 3

class HitObjectAttributes(int, Enum):
    X = 0
    Y = 1
    TIME = 2
    OBJ_TYPE = 3
    HITSOUND = 4
    HITSAMPLE = 5

class HitsoundBits(int, Enum):
    NORMAL = 1
    WHISTLE = 2
    FINISH = 4
    CLAP = 8

def is_mode_taiko(dot_osu_line: str) -> bool:

    k, _, mode_str = dot_osu_line.partition(':')
    return int(mode_str) == Gamemode.TAIKO

def append_seed_to_diffname(dot_osu_line: str, seed: int) -> str:

    line_str = dot_osu_line.strip()
    seed_str = int_to_hex_string(seed)

    return f"{line_str} {seed_str}\n"

def flip_object_hitsound(dot_osu_line: str) -> str: # kat -> don and vice versa (preserving finisher)

    attributes = dot_osu_line.split(',')

    # slider spinner or blank, ignore
    if len(attributes) != len(HitObjectAttributes):
        return dot_osu_line

    hitsound = attributes[HitObjectAttributes.HITSOUND]
    attributes[HitObjectAttributes.HITSOUND] = _get_flipped_hitsound(hitsound)

    return ','.join(attributes)

def _get_flipped_hitsound(hitsound_str: str) -> str:
    
    hitsound = int(hitsound_str)

    if hitsound & HitsoundBits.CLAP:
        return str(hitsound - HitsoundBits.CLAP)

    if hitsound & HitsoundBits.WHISTLE:
        return str(hitsound - HitsoundBits.WHISTLE)

    return str(hitsound + HitsoundBits.CLAP)
