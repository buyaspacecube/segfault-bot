from pathlib import Path
from pandas import read_csv

def get_slots() -> list[str]:

    path_to_mappool = Path() / "mappool" / "mappool.csv"
    mappool = read_csv(path_to_mappool)

    return mappool['slot'].tolist()

def get_name_for_packaged_osz(slot: str) -> str:

    path_to_mappool = Path() / "mappool" / "mappool.csv"
    mappool = read_csv(path_to_mappool)

    # pandas is scary
    setID, artist, title = mappool.loc[
        mappool['slot'] == slot,
        ['setID', 'artist', 'title']
    ].values.flatten().tolist()

    return f"{setID} {artist} - {title}.osz"
