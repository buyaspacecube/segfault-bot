from random import sample, seed as set_seed

from repository.getters import get_slots

full_range = range(0, 2**16)

# arbitrarily chosen
practice_seeds = [10782, 38831, 3366, 24974, 49061, 49360, 46106, 18885, 15259, 8068]

range_minus_practice = [s for s in full_range if s not in practice_seeds]

def get_random_seeds(diffs: int) -> list[int]:

    set_seed(None)
    return sample(full_range, diffs)

def get_match_seeds(match_ID: int) -> dict[str, int]:

    match_seeds: dict[str, int] = dict()

    slots: list[str] = get_slots()
    slot_count = len(slots)

    set_seed(match_ID)

    seeds: list[int] = sample(range_minus_practice, slot_count)

    zipped = zip(slots, seeds)
    return dict(zipped)

def get_practice_seeds() -> list[int]:
    return practice_seeds
