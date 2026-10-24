from discord import DiscordException

from discord.errors import Forbidden
from discord.ext.commands.errors import NoPrivateMessage

from discord.ext.commands import Cog

class Error(Cog):

    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_application_command_error(self, ctx, error: DiscordException):

        if isinstance(error, Forbidden):
            await ctx.respond("ERROR: You do not have permission to use this command")

        elif isinstance(error, NoPrivateMessage):
            await ctx.respond("ERROR: This command cannot be used in direct messages")

        else:
            
            await ctx.respond("Unknown error, report it to Eloise")
            raise error

# add to bot
def setup(bot):

    error = Error(bot)
    bot.add_cog(error)
