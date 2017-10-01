from discord.ext import commands
from discord.ext.commands import when_mentioned_or

from comet.logging import LoggingClass


class Comet(LoggingClass, commands.Bot):
    def __init__(self, cfg):
        # Setup.
        commands.Bot.__init__(self, command_prefix=when_mentioned_or('!'))
        LoggingClass.__init__(self)

        self.cfg = cfg

    async def on_ready(self):
        # Ready!
        self.log.info('Ready! Logged in as %s (%d)', self.user, self.user.id)

    async def on_message(self, message):
        # Ignore messages from ourselves or bots.
        if message.author == self.user or message.author.bot:
            return

        # Invoke commands.
        ctx = await self.get_context(message)
        await self.invoke(ctx)

