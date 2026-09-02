from random import sample, seed as set_seed, choices

def generate_seeds(diffs: int) -> list[int]:

    seed_range = range(0, 2**16)
    return sample(seed_range, diffs)

def generate_flips(object_count: int, seed: int) -> list[bool]:

    options = [True, False]

    set_seed(seed)
    return choices(options, k = object_count)
