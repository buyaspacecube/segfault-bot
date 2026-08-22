from random import sample

def generate_seeds(diffs: int, seed: int) -> list[int]:

    if diffs == 1 and seed:
        return [seed]

    seed_range = range(0, 2**16)
    return sample(seed_range, diffs)
