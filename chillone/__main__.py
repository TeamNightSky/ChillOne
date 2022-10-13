import os
import nextcord
from typing import Iterable

from nextcord.ext import tasks

from chillone.space import Space


def embed(*args, fields: Iterable[tuple[str, ...]]=(), inline: bool = False, **kwargs) -> nextcord.Embed:
    temp = nextcord.Embed(*args, **kwargs)
    for name, value in fields:
        temp.add_field(name=name, value=value, inline=inline)
    return temp


class ChillOneBot(nextcord.Client):
    """The Chill One source code."""

    @tasks.loop(hours=24*7)
    async def chill(self, ) -> None:
        """Send chill vibes to the chill vibes channel."""
        for server in self.guilds:
            for channel in server.channels:
                if "chill-vibes" in channel.name.lower():
                    for _ in range(42):
                        await channel.send("".join(Space.generate(1800)))
                    return


if __name__ == "__main__":
    bot = ChillOneBot()
    bot.run(os.environ["BOT_TOKEN"])
