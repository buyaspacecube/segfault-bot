from io import BytesIO

from generator.osz_bytes.detarame_converter import convert
from generator.osz_bytes.package_osus_into_osz_bytes import package_osus_into_osz_bytes
from repository.path import path_to_osu

def generate_osz_bytes(slot: str, seeds: list[int], osu_only: bool = False, is_match: bool = False) -> BytesIO:

    original_osu: str = str()

    with open(path_to_osu(slot), mode='r', encoding='utf-8') as f:
        original_osu = f.read()

    converted_osus: dict[int, str] = dict()

    for seed in seeds:

        converted = convert(original_osu, seed, is_match)
        converted_osus[seed] = converted

    return package_osus_into_osz_bytes(converted_osus, slot, osu_only)
