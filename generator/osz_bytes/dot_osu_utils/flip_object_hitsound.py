from generator.osz_bytes.dot_osu_utils.enums import HitObjectAttributes, HitsoundBits

def flip_object_hitsound(dot_osu_line: str) -> str: # kat -> don and vice versa (preserving finisher)

    attributes = dot_osu_line.split(',')

    # slider spinner or blank, ignore
    if len(attributes) != len(HitObjectAttributes):
        return dot_osu_line

    hitsound = attributes[HitObjectAttributes.HITSOUND]
    attributes[HitObjectAttributes.HITSOUND] = _get_flipped_hitsound(hitsound)

    return ','.join(attributes)

def _get_flipped_hitsound(hitsound_str: str) -> str:
    
    hitsound = int(hitsound_str)

    if hitsound & HitsoundBits.CLAP:
        return str(hitsound - HitsoundBits.CLAP)

    if hitsound & HitsoundBits.WHISTLE:
        return str(hitsound - HitsoundBits.WHISTLE)

    return str(hitsound + HitsoundBits.CLAP)

