from typing import final
from collections.abc import Sequence

from jardiscordengine.interns.extern import JTKExternError
from jardiscordengine.interns.decorators import documented


@final
@documented
class JDETerminalRestart(JTKExternError.JErrorSystem):

    pass


__all__: Sequence[str] = [
    "JDETerminalRestart",
]
