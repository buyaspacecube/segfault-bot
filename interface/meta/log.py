from discord.ext.commands import Cog
from datetime import datetime

class Log(Cog):

    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_application_command(self, ctx):

        timestamp = datetime.now()
        user = ctx.author.name
        command = ctx.command.qualified_name

        log = f"[{timestamp}] {user} used /{command}"

        for option in ctx.selected_options:

            name, value = option.get('name'), option.get('value')
            log += f" {name}:{value}"
            
        print(log)

# add to bot
def setup(bot):

    log = Log(bot)
    bot.add_cog(log)
