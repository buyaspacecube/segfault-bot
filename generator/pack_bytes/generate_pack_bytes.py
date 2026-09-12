from io import BytesIO
from zipfile import ZipFile

from generator.osz_bytes.generate_osz_bytes import generate_osz_bytes
from repository.getters import get_name_for_packaged_osz

def generate_pack_bytes(slots: list[str], seed_lists: list[list[int]], osu_only: bool = False) -> BytesIO:

    if len(slots) != len(seed_lists):
        raise ValueError("Slots and seed lists must be same length")

    pack_bytes: BytesIO = BytesIO()
    pack_zip: ZipFile = ZipFile(pack_bytes, mode='w')

    for slot, seeds in zip(slots, seed_lists):

        osz_bytes = generate_osz_bytes(slot, seeds, osu_only)
        osz_data = osz_bytes.getvalue()

        filename = get_name_for_packaged_osz(slot)

        pack_zip.writestr(filename, osz_data)

    pack_zip.close()
    
    pack_bytes.seek(0)
    return pack_bytes
