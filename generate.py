from io import BytesIO
from random import sample

from converter.convert import convert

from repository.package import package
from repository.utils import path_to_osu

def generate(slot: str, diffs: int) -> BytesIO: # .osz bytes

    original_osu: str = str()

    with open(path_to_osu(slot), mode='r', encoding='utf-8') as f:
        original_osu = f.read()

    seed_range = range(0, 2**16)
    seeds = sample(seed_range, diffs)

    converted_osus: list[str] = list()

    for i in range(diffs):

        converted = convert(original_osu, seeds[i])
        converted_osus.append(converted)
    
    return package(converted_osus, slot)
