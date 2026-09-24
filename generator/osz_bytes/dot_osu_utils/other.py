from generator.osz_bytes.dot_osu_utils.enums import Gamemode

def is_mode_taiko(dot_osu_line: str) -> bool:

    k, _, mode_str = dot_osu_line.partition(':')
    return int(mode_str) == Gamemode.TAIKO

def append_to_line(line: str, content: str) -> str:

    stripped = line.strip()
    return stripped + " " + content + "\n"
