"""
JarDiscordEngine - Terminals

Terminal creation, command creation and handling.
"""

from collections.abc import Sequence

from .decorator import (
    terminal_command,
)
from .terminal import (
    JDETerminal,
)

__all__: Sequence[str] = [
    "JDETerminal",
    "terminal_command",
]
