from io import BytesIO
from zipfile import ZipFile

from generator.osz_bytes.generate_osz_bytes import generate_osz_bytes
from repository.getters import get_name_for_packaged_osz

def generate_pack_bytes(slots: list[str], seeds: list[int], osu_only: bool = False) -> BytesIO:

    if len(slots) != len(seeds):
        raise ValueError("Slots and seeds must be same length")

    pack_bytes: BytesIO = BytesIO()
    pack_zip: ZipFile = ZipFile(pack_bytes, mode='w')

    for slot, seed in zip(slots, seeds):

        osz_bytes = generate_osz_bytes(slot, [seed], osu_only)
        osz_data = osz_bytes.getvalue()

        filename = get_name_for_packaged_osz(slot)

        pack_zip.writestr(filename, osz_data)

    pack_zip.close()
    
    pack_bytes.seek(0)
    return pack_bytes
