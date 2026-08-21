from converter.utils import is_mode_taiko, append_seed_to_diffname, generate_object_flips, flip_object_hitsound

def convert(original_osu: str, seed: int) -> str:

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
            osu_lines[line_index] = append_seed_to_diffname(line, seed)

        if line.startswith('[HitObjects]'):

            object_count = len(osu_lines) - line_index
            object_flips = generate_object_flips(object_count, seed)

            is_processing_objects = True
            continue

        if is_processing_objects:

            object_index += 1

            if object_flips[object_index]:
                osu_lines[line_index] = flip_object_hitsound(line)

    converted_osu = '\n'.join(osu_lines)
    return converted_osu

