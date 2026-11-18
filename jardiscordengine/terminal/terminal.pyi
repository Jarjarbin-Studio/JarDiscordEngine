from collections.abc import Awaitable, Callable
from typing import final

from jardiscordengine.bots.bot import JDEBot
from jardiscordengine.interns.base_classe import JDEInternBaseClass
from jardiscordengine.interns.decorators import documented, logged, timed
from jardiscordengine.interns.enums import JDEInternInstancePolicy
from jardiscordengine.interns.extern import JTKExternError

class JDETerminalRestart(JTKExternError.JErrorSystem):
    """Raise to the JarDiscordEngine a restart signal/exception"""

@final
class JDETerminal(
    JDEInternBaseClass[
        JDEInternInstancePolicy.SINGLETON,
        1,
        True,
    ]
):
    """
    Terminal handler.

    Attributes:
        on_starting (Callable[[], Awaitable[None]] | None): Function that will be called when terminal AND bot starting.
        on_start (Callable[[], Awaitable[None]] | None): Function that will be called when terminal AND bot started.
        on_closing (Callable[[], Awaitable[None]] | None): Function that will be called when terminal AND bot closing.
        on_close (Callable[[], Awaitable[None]] | None): Function that will be called when terminal AND bot closed.
    """

    on_starting: Callable[[], Awaitable[None]] | None = None
    on_started: Callable[[], Awaitable[None]] | None = None
    on_closing: Callable[[], Awaitable[None]] | None = None
    on_closed: Callable[[], Awaitable[None]] | None = None

    def __init__(
        self,
        bot: JDEBot,
        prompt: str | None = None,
        on_starting: Callable[[], Awaitable[None]] | None = None,
        on_started: Callable[[], Awaitable[None]] | None = None,
        on_closing: Callable[[], Awaitable[None]] | None = None,
        on_closed: Callable[[], Awaitable[None]] | None = None
    ) -> None:
        """
        Create a terminal.

        Args:
            bot (JDEBot): Bot.
            prompt (str | None): Terminal command prompt.
            on_starting (Callable[[], Awaitable[None]] | None): Function that will be called when terminal AND bot starting.
            on_started (Callable[[], Awaitable[None]] | None): Function that will be called when terminal AND bot started.
            on_closing (Callable[[], Awaitable[None]] | None): Function that will be called when terminal AND bot closing.
            on_closed (Callable[[], Awaitable[None]] | None): Function that will be called when terminal AND bot closed.
        """

    @property
    def bot(
        self
    ) -> JDEBot:
        """
        Get linked bot.

        Returns:
            JDEBot: Bot linked to the terminal.
        """

    @property
    def commands(
        self
    ) -> dict[str, Callable[[list[str]], Awaitable[None]]]:
        """
        Get registered commands.

        Returns:
            dict[str, Callable[[list[str]], Awaitable[None]]]: Commands.
        """

    def register_command(
        self,
        handler: Callable[[list[str]], Awaitable[None]]
    ) -> None:
        """
        Register a terminal command.

        Args:
            handler (Callable[[list[str]], Awaitable[None]]): Command handler.
        """

    def register_commands(
        self,
        *handlers: Callable[[list[str]], Awaitable[None]]
    ) -> None:
        """
        Register terminal commands in batch.

        Args:
            *handlers (Callable[[list[str]], Awaitable[None]]): Command handlers.
        """

    async def run(
        self
    ) -> None:
        """Run the terminal interface."""
