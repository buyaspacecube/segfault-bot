from generator.osz_bytes.dot_osu_utils.other import is_mode_taiko, append_to_line
from generator.osz_bytes.dot_osu_utils.flip_object_hitsound import flip_object_hitsound
from generator.osz_bytes.get_flips import get_flips

from interface.strings import int_to_hex_string

def convert(original_osu: str, seed: int, is_match: bool = False) -> str:

    object_flips: list[bool] = list()
    is_processing_objects = False

    osu_lines: list[str] = original_osu.split('\n')

    line_index: int = -1
    object_index: int = -1

    for line in osu_lines:

        line_index += 1

        if line.startswith('Mode:'):
            
            if not is_mode_taiko(line):
                raise TypeError("Map must be taiko")

        if line.startswith('Version:'):

            seed_hex = int_to_hex_string(seed)
            osu_lines[line_index] = append_to_line(line, seed_hex)

        if line.startswith('Tags:'):

            match_tag = "?match" if is_match else ""
            tags = f"?converted ?segfault {match_tag}"
            osu_lines[line_index] = append_to_line(line, tags)

        if line.startswith('[HitObjects]'):

            object_count = len(osu_lines) - line_index
            object_flips = get_flips(object_count, seed)

            is_processing_objects = True
            continue

        if is_processing_objects:

            object_index += 1

            if object_flips[object_index]:
                osu_lines[line_index] = flip_object_hitsound(line)

    converted_osu = '\n'.join(osu_lines)
    return converted_osu
