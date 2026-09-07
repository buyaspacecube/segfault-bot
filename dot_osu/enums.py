from enum import Enum

class Gamemode(int, Enum):
    OSU = 0
    TAIKO = 1
    CATCH = 2
    MANIA = 3

class HitObjectAttributes(int, Enum):
    X = 0
    Y = 1
    TIME = 2
    OBJ_TYPE = 3
    HITSOUND = 4
    HITSAMPLE = 5

class HitsoundBits(int, Enum):
    NORMAL = 1
    WHISTLE = 2
    FINISH = 4
    CLAP = 8
