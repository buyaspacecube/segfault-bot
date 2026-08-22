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

def get_slots() -> list[str]:

    osu_dir = Path() / "repository" / "osu"
    files = osu_dir.iterdir()
    
    slots = [f.stem for f in files]
    slots_sorted: list[str] = list()

    groups = ["NM", "HD", "HR", "FM", "EX"]

    for group in groups:
        
        slots_in_group = [s for s in slots if s.startswith(group)]
        list.sort(slots_in_group)
        
        slots_sorted += slots_in_group

    return slots_sorted

