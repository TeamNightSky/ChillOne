import random


class Space:
    characters: dict[str, int] = {
        " ": 50000,
        ".": 500,
        "✦": 400,
        "˚": 400,
        ":comet:": 10,
        ",": 200,
        "　ﾟ": 300,
        ":sunny:": 2,
        ":earth_americas:": 10,
        "*": 50,
        ":sun_with_face:": 0,
        ":star:": 10,
        ":sparkles:": 10,
        ":full_moon:": 10,
        ":new_moon:": 2,
        ":ringed_planet:": 2,
    }

    @classmethod
    def generate(cls, length: int) -> list[str]:
        return random.choices(
                list(cls.characters.keys()),
                weights=list(cls.characters.values()),
                k=length,
            )