from discord import Member

from repository.getters import get_slots, get_full_title, get_beatmap_link

def int_to_hex_string(i: int):
    return "0x" + f"{i:X}".zfill(4)

def get_generated_seeds_message(seeds: list[int]) -> str:

    str_seeds = [int_to_hex_string(seed) for seed in seeds]
    s = "s" if len(seeds) > 1 else ""

    return f"Generated seed{s} **{', '.join(str_seeds)}**"

lobby_created_string = """
{players} your {match_or_lobby} is starting soon!

{staff}
"""

def get_lobby_created_message(players: list[Member], staff: dict[str, Member], is_match: bool) -> str:

    player_mentions = [p.mention for p in players]
    staff_mentions = [f"{s.mention} will be your {role}" for role, s in staff.items()]

    return lobby_created_string.format(
        players = ' '.join(player_mentions),
        staff = '\n'.join(staff_mentions),
        match_or_lobby = "match" if is_match else "lobby"
    )

referee_seeds_string = """
Seeds for **{lobby_title}**
Copy these using the copy button at the top right, then paste onto the ref sheet!

```
{seeds}
```
"""

def get_referee_seeds_message(lobby_title: str, seeds: list[int]) -> str:

    hex_seeds = [int_to_hex_string(s) for s in seeds]

    return referee_seeds_string.format(
        lobby_title = lobby_title,
        seeds = '\n'.join(hex_seeds)
    )

streamer_pack_string = """
Generated maps for **{lobby_title}**
This includes .osu files ONLY! Make sure you already have the full mappool before downloading
After downloading, restart your stable streaming client
"""

def get_streamer_pack_message(lobby_title: str) -> str:

    return streamer_pack_string.format(
        lobby_title = lobby_title
    )

top_mappool_string = """
# [Download practice pack](<{pack_link}>)

{nomod_maps}
** **
"""

middle_mappool_string = """
{mod_maps}
** **
"""

bottom_mappool_string = """
{EX_maps}
"""

def get_square(slot: str) -> str:

    if slot.startswith('NM'): return ":white_large_square:"
    if slot.startswith('HD'): return ":yellow_square:"
    if slot.startswith('HR'): return ":red_square:"
    if slot.startswith('FM'): return ":blue_square:"
    if slot.startswith('EX'): return ":purple_square:"

    raise ValueError("Invalid slot")

def get_map_string(slot: str) -> str:

    square = get_square(slot)
    title = get_full_title(slot)
    link = get_beatmap_link(slot)

    return f"{square} `{slot}` [{title}]({link})"

def get_mappool_messages(practice_pack_link: str) -> list[str]:

    slots = get_slots()

    nomod_map_strings = [
        get_map_string(s) for s in slots
        if s.startswith('NM')
    ]

    mod_map_strings = [
        get_map_string(s) for s in slots
        if s.startswith('HD') or s.startswith('HR') or s.startswith('FM')
    ]

    EX_map_strings = [
        get_map_string(s) for s in slots
        if s.startswith('EX')
    ]

    # surely a nicer way to do this but whatever
    return [
        top_mappool_string.format(
            pack_link = practice_pack_link,
            nomod_maps = '\n'.join(nomod_map_strings)
        ),
        middle_mappool_string.format(
            mod_maps = '\n'.join(mod_map_strings)
        ),
        bottom_mappool_string.format(
            EX_maps = '\n'.join(EX_map_strings)
        )
    ]
