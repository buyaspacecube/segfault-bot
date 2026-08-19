from converter.utils import is_mode_taiko, append_seed_to_diffname, generate_object_flips, flip_object_hitsound

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
                converted_osu_lines[line_index] = flip_object_hitsound(line)

    return converted_osu_lines
