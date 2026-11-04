from pathlib import Path
from pandas import read_csv, isnull

def get_slots() -> list[str]:

    path_to_mappool = Path() / "repository" / "mappool" / "mappool.csv"
    mappool = read_csv(path_to_mappool)

    return mappool['slot'].tolist()

def get_name_for_converted_osu(slot: str, seed: int) -> str:

    path_to_mappool = Path() / "repository" / "mappool" / "mappool.csv"
    mappool = read_csv(path_to_mappool)

    artist, title = mappool.loc[
        mappool['slot'] == slot,
        ['artist', 'title']
    ].values.flatten().tolist()

    name: str = str()

    if isnull(artist):
        name = title

    else:
        name = f"{artist} - {title}"

    # replace characters that are weird in filenames
    name_sanitised = name.replace('|', '').replace('?', '').replace('/', '')
    
    return name_sanitised

def get_name_for_packaged_osz(slot: str) -> str:

    path_to_mappool = Path() / "repository" / "mappool" / "mappool.csv"
    mappool = read_csv(path_to_mappool)

    setID, artist, title = mappool.loc[
        mappool['slot'] == slot,
        ['setID', 'artist', 'title']
    ].values.flatten().tolist()

    name: str = str()

    if isnull(artist):
        name = f"{setID} - {title}.osz"

    else:
        name = f"{setID} {artist} - {title}.osz"

    # more filename trial and error
    name_sanitised = name.replace('?', '').replace('/', '_')

    return name_sanitised

def get_full_title(slot: str) -> str:

    path_to_mappool = Path() / "repository" / "mappool" / "mappool.csv"
    mappool = read_csv(path_to_mappool)

    artist, title, diffname = mappool.loc[
        mappool['slot'] == slot,
        ['artist', 'title', 'diffname']
    ].values.flatten().tolist()

    if isnull(artist):
        return f"{title} [{diffname}]"

    return f"{artist} - {title} [{diffname}]"

def get_beatmap_link(slot: str) -> str:

    path_to_mappool = Path() / "repository" / "mappool" / "mappool.csv"
    mappool = read_csv(path_to_mappool)

    diffID = mappool.loc[
        mappool['slot'] == slot,
        'diffID'
    ].values[0]

    return f"<https://osu.ppy.sh/b/{diffID}>"
