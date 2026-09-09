from random import sample

def get_seeds(diffs: int) -> list[int]:

    seed_range = range(0, 2**16)
    return sample(seed_range, diffs)
