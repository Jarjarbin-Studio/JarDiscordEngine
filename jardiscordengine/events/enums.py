# =============================================================================
# JarDiscordEngine - Python Discord Bot Engine (pycord-based)
# =============================================================================
#
# JarDiscordEngine is a lightweight bot framework built on top of pycord
# that simplifies Discord bot development while providing higher-level
# abstractions for command management, event handling, and extensibility.
#
# =============================================================================
# Version: jardiscordengine-v1
# Author: Jarjarbin Studio
# License: GPL v3
# =============================================================================
#
# This engine is inspired by pycord, modern bot framework design patterns,
# and modular software architecture.
#
# It is designed for educational purposes and small-to-medium Discord bot
# projects.
#
# It provides structured systems such as automatic command discovery,
# command registration, event handling, extension management, and shared
# services for logging, configuration, and permissions.
#
# =============================================================================
# WARNING:
# =============================================================================
#
# This is NOT pycord itself.
# It is a custom abstraction layer built on top of pycord.
#
# =============================================================================

from __future__ import annotations

from enum import IntEnum as _IntEnum
from enum import auto as _auto
from typing import final as _final


@_final
class JDEEventType(_IntEnum):

    # Messages
    MESSAGE_SENT = _auto()
    MESSAGE_EDITED = _auto()
    MESSAGE_DELETED = _auto()
    MESSAGE_BULK_DELETED = _auto()
    BOT_MENTIONED = _auto()
    MESSAGE_PINNED = _auto()
    MESSAGE_UNPINNED = _auto()

    # Reactions
    REACTION_ADDED = _auto()
    REACTION_REMOVED = _auto()

    # Users
    USER_JOINED = _auto()
    USER_LEFT = _auto()
    USER_UPDATED = _auto()

    # Members
    MEMBER_BANNED = _auto()
    MEMBER_UNBANNED = _auto()
    MEMBER_KICKED = _auto()
    MEMBER_UPDATED = _auto()

    # Guilds
    GUILD_JOINED = _auto()
    GUILD_LEFT = _auto()
    GUILD_UPDATED = _auto()

    # Channels
    CHANNEL_CREATED = _auto()
    CHANNEL_UPDATED = _auto()
    CHANNEL_DELETED = _auto()
    CHANNEL_OVERWRITES_UPDATED = _auto()
    VOICE_STATE_UPDATED = _auto()

    # Categories
    CATEGORY_CREATED = _auto()
    CATEGORY_UPDATED = _auto()
    CATEGORY_DELETED = _auto()

    # Roles
    ROLE_CREATED = _auto()
    ROLE_UPDATED = _auto()
    ROLE_DELETED = _auto()
    ROLE_ASSIGNED = _auto()
    ROLE_REMOVED = _auto()

    # Threads
    THREAD_CREATED = _auto()
    THREAD_DELETED = _auto()

    # Invites
    INVITE_CREATED = _auto()
    INVITE_DELETED = _auto()

    # Miscellaneous
    BUTTON_CLICKED = _auto()
    SELECT_MENU_USED = _auto()

__all__ = [
    "JDEEventType",
]
