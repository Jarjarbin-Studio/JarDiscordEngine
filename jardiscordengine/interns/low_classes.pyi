from collections.abc import Sequence

from jardiscordengine.interns.base_classe import (
    JDEInternBaseClass,
)

class JDEInternEntity(
    JDEInternBaseClass
):
    """Entity (used for typing mostly)."""

    def __init__(
        self
    ) -> None:
        """Initialize an entity."""

class JDEInternField(
    JDEInternBaseClass
):
    """Field (used for typing mostly)."""

    def __init__(self):
        """Initialize a field."""

__all__: Sequence[str] = [
    "JDEInternEntity",
    "JDEInternField",
]
