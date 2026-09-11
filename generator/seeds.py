from random import sample, seed as set_seed

from repository.getters import get_slots

seed_range = range(0, 2**16)

def get_random_seeds(diffs: int) -> list[int]:

    set_seed(None)
    return sample(seed_range, diffs)

def get_match_seeds(match_ID: int) -> dict[str, int]:

    match_seeds: dict[str, int] = dict()

    slots: list[str] = get_slots()
    slot_count = len(slots)

    set_seed(match_ID)

    seeds: list[int] = sample(seed_range, slot_count)

    zipped = zip(slots, seeds)
    return dict(zipped)
