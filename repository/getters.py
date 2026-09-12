from pathlib import Path
from pandas import read_csv

def get_slots() -> list[str]:

    path_to_mappool = Path() / "repository" / "mappool" / "mappool.csv"
    mappool = read_csv(path_to_mappool)

    return mappool['slot'].tolist()

def get_name_for_packaged_osz(slot: str) -> str:

    path_to_mappool = Path() / "repository" / "mappool" / "mappool.csv"
    mappool = read_csv(path_to_mappool)

    setID, artist, title = mappool.loc[
        mappool['slot'] == slot,
        ['setID', 'artist', 'title']
    ].values.flatten().tolist()

    return f"{setID} {artist} - {title}.osz"

def get_full_title(slot: str) -> str:

    path_to_mappool = Path() / "repository" / "mappool" / "mappool.csv"
    mappool = read_csv(path_to_mappool)

    artist, title, diffname = mappool.loc[
        mappool['slot'] == slot,
        ['artist', 'title', 'diffname']
    ].values.flatten().tolist()

    return f"{artist} - {title} [{diffname}]"

def get_beatmap_link(slot: str) -> str:

    path_to_mappool = Path() / "repository" / "mappool" / "mappool.csv"
    mappool = read_csv(path_to_mappool)

    diffID = mappool.loc[
        mappool['slot'] == slot,
        'diffID'
    ].values[0]

    return f"<https://osu.ppy.sh/b/{diffID}>"
