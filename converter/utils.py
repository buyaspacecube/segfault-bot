from enum import Enum
import random

#
# gamemode stuff
#
class Gamemode(int, Enum):
    OSU = 0
    TAIKO = 1
    CATCH = 2
    MANIA = 3

def is_mode_taiko(dot_osu_line: str) -> bool:
    
    k, _, mode_str = dot_osu_line.partition(':')
    return int(mode_str) == Gamemode.TAIKO

#
# diffname stuff
#
def int_to_hex_string(i: int):
    return "0x" + f"{i:X}".zfill(4)

def append_seed_to_diffname(line: str, seed: int) -> str:
    return f"{line.strip()} {int_to_hex_string(seed)}\n"

#
# hitsound stuff
#
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

def flip_object_hitsound(dot_osu_line: str) -> str: # kat -> don and vice versa (preserving finisher)

    attributes = dot_osu_line.split(',')

    # slider or spinner, ignore
    if len(attributes) > len(HitObjectAttributes):
        return dot_osu_line

    hitsound = attributes[HitObjectAttributes.HITSOUND]
    attributes[HitObjectAttributes.HITSOUND] = flip_hitsound(hitsound)

    return ','.join(attributes)

def flip_hitsound(hitsound_str: str) -> str:
    
    hitsound = int(hitsound_str)

    if hitsound & HitsoundBits.CLAP:
        return str(hitsound - HitsoundBits.CLAP)

    if hitsound & HitsoundBits.WHISTLE:
        return str(hitsound - HitsoundBits.WHISTLE)

    return str(hitsound + HitsoundBits.CLAP)

#
# generate list of true and false determining which objects get flipped
#
def generate_object_flips(object_count: int, seed: int) -> list[bool]:

    options = [True, False]

    random.seed(seed)
    return random.choices(options, k = object_count)
