from io import BytesIO

from generator.utils import generate_seeds

from converter.convert import convert

from repository.package import package
from repository.utils import path_to_osu

def generate(slot: str, diffs: int, seed: int = None) -> BytesIO: # .osz bytes

    original_osu: str = str()

    with open(path_to_osu(slot), mode='r', encoding='utf-8') as f:
        original_osu = f.read()

    seeds: list[int] = generate_seeds(diffs, seed)

    converted_osus: dict[int, str] = dict()

    for i in range(diffs):

        seed = seeds[i]

        converted = convert(original_osu, seed)
        converted_osus[seed] = converted
    
    return package(converted_osus, slot)

