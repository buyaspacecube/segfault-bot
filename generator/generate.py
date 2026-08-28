from io import BytesIO
from discord import File

from converter.convert import convert

from repository.package import package
from repository.utils import path_to_osu, get_name_for_packaged_osz

def generate(slot: str, diffs: int, seeds: list[int]) -> File:
    original_osu: str = str()

    with open(path_to_osu(slot), mode='r', encoding='utf-8') as f:
        original_osu = f.read()

    converted_osus: dict[int, str] = dict()

    for i in range(diffs):

        seed = seeds[i]

        converted = convert(original_osu, seed)
        converted_osus[seed] = converted
    
    osz_bytes: BytesIO = package(converted_osus, slot)
    filename = get_name_for_packaged_osz(slot)

    return File(osz_bytes, filename=filename)

