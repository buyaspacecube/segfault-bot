from random import seed as set_seed, choices

def generate_flips(object_count: int, seed: int) -> list[bool]:

    options = [True, False]

    set_seed(seed)
    return choices(options, k = object_count)
