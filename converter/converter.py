from enum import Enum
from io import StringIO
import random


def int_to_hex_string(i: int):
    return "0x" + f"{i:X}".zfill(4)

def append_seed_to_diffname(line: str, seed: int) -> str:
    return f"{line.strip()} {int_to_hex_string(seed)}\n"


def generate_object_flips(object_count: int, seed: int) -> list[bool]:

    options = [True, False]

    random.seed(seed)
    return random.choices(options, k = object_count)


MODE_TAIKO = 1

def is_mode_taiko(line: str) -> bool:

    k, _, mode_str = line.partition(':')
    return int(mode_str) == MODE_TAIKO


class HitsoundBits(int, Enum):
    NORMAL = 1
    WHISTLE = 2
    FINISH = 4
    CLAP = 8
    
def flip_hitsound(hitsound_str: str) -> str:
    
    hitsound = int(hitsound_str)

    if hitsound & HitsoundBits.CLAP:
        return str(hitsound - HitsoundBits.CLAP)

    if hitsound & HitsoundBits.WHISTLE:
        return str(hitsound - HitsoundBits.WHISTLE)

    return str(hitsound + HitsoundBits.CLAP)


class HitObjectAttributes(int, Enum):
    X = 0
    Y = 1
    TIME = 2
    OBJ_TYPE = 3
    HITSOUND = 4
    HITSAMPLE = 5

def flip_object(line: str) -> str:

    attributes = line.split(',')

    # slider or spinner, ignore
    if len(attributes) > len(HitObjectAttributes):
        return line

    hitsound = attributes[HitObjectAttributes.HITSOUND]
    attributes[HitObjectAttributes.HITSOUND] = flip_hitsound(hitsound)

    return ','.join(attributes)


#
# main method
#
def convert(original_osu_lines: list[str], seed: int) -> list[str]:

    converted_osu_lines: list[str] = original_osu_lines

    object_flips: list[bool] = list()
    is_processing_objects = False

    line_index: int = -1
    object_index: int = -1

    for line in original_osu_lines:

        line_index += 1

        if line.startswith('Mode:'):
            if not is_mode_taiko(line):
                raise TypeError("Map must be taiko")

        if line.startswith('Version:'):
            converted_osu_lines[line_index] = append_seed_to_diffname(line, seed)

        if line.startswith('[HitObjects]'):

            object_count = len(original_osu_lines) - line_index
            object_flips = generate_object_flips(object_count, seed)

            is_processing_objects = True
            continue

        if is_processing_objects:

            object_index += 1

            if object_flips[object_index]:
                converted_osu_lines[line_index] = flip_object(line)

    return converted_osu_lines

    
