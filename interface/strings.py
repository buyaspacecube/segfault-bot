from discord import Member

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
