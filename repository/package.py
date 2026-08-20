from io import BytesIO
from zipfile import ZipFile

from repository.utils import path_to_osz_template

from converter.utils import int_to_hex_string

def package(converted_osus: dict[int, str], slot: str) -> BytesIO: # .osz bytes

    packaged_osz_bytes: BytesIO = BytesIO()

    with open(path_to_osz_template(slot), mode='rb') as f:

        template_osz: ZipFile = ZipFile(f)
        packaged_osz: ZipFile = ZipFile(packaged_osz_bytes, mode='w')

        for item in template_osz.infolist():

            file_data = template_osz.read(item.filename)
            packaged_osz.writestr(item, file_data)

        for seed, osu in converted_osus.items():

            filename = f"{int_to_hex_string(seed)}.osu"
            packaged_osz.writestr(filename, osu)

        template_osz.close()
        packaged_osz.close()

    packaged_osz_bytes.seek(0)
    return packaged_osz_bytes
