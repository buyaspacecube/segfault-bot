from pathlib import Path

def path_to_osu(slot: str) -> str:

    path = Path() / "repository" / "osu" / f"{slot}.osu"

    if not path.exists():
        raise OSError(".osu not found")

    return path

def path_to_osz_template(slot: str) -> str:

    path = Path() / "repository" / "osz_template" / f"{slot}.osz"

    if not path.exists():
        raise OSError(".osz template not found")

    return path
