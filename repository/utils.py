from pathlib import Path
from pandas import read_csv

def path_to_osu(slot: str) -> str:

    path = Path() / "mappool" / "osu" / f"{slot}.osu"

    if not path.exists():
        raise OSError(".osu not found")

    return path

def path_to_osz_template(slot: str) -> str:

    path = Path() / "mappool" / "osz_template" / f"{slot}.osz"

    if not path.exists():
        raise OSError(".osz template not found")

    return path

def get_name_for_packaged_osz(slot: str) -> str:

    path_to_mappool = Path() / "mappool" / "mappool.csv"
    mappool = read_csv(path_to_mappool)

    # pandas is scary
    setID, artist, title = mappool.loc[
        mappool['slot'] == slot,
        ['setID', 'artist', 'title']
    ].values.flatten().tolist()

    return f"{setID} {artist} - {title}.osz"

def get_slots() -> list[str]:

    path_to_mappool = Path() / "mappool" / "mappool.csv"
    mappool = read_csv(path_to_mappool)

    return mappool['slot'].tolist()

