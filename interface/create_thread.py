from discord import slash_command, SlashCommandGroup
from discord.ext.commands import Cog

from interface.options import get_player_option, get_streamer_option

player1_option, player2_option = get_player_option(1), get_player_option(2)
streamer_option = get_streamer_option()

match_start_string = """
{p1} and {p2}, your match is starting soon!

{ref} will be your referee
{stream} will be your streamer
"""

class CreateThread(Cog):

    def __init__(self, bot):
        self.bot = bot

    create = SlashCommandGroup(name="create")

    @create.command(name="thread", description="(REFEREE ONLY) Create the thread for a Segfault Cup match")
    async def command_create_thread(self, ctx,
                                    player1: player1_option,
                                    player2: player2_option,
                                    streamer: streamer_option):

        referee = ctx.author

        match_start_string_formatted = match_start_string.format(
            p1 = player1.mention,
            p2 = player2.mention,
            ref = referee.mention,
            stream = streamer.mention
        )

        message = await ctx.send(match_start_string_formatted)
        await message.create_thread(name=f"{player1.nick} vs. {player2.nick}")

# add to bot
def setup(bot):

    create_thread = CreateThread(bot)
    bot.add_cog(create_thread)
