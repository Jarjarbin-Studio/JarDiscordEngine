from collections.abc import Sequence
from enum import IntEnum, StrEnum
from typing import final

@final
class JDEEventType(IntEnum):
    """
    Discord event type.

    All events include the ones triggered by the bot,
    filter them with condition decorators.

    Attributes:
        # Messages
        MESSAGE_SENT (int): Message sent.
        MESSAGE_EDITED (int): Message edited.
        MESSAGE_DELETED (int): Message deleted.
        MESSAGE_BULK_DELETED (int): Bulk message deleted.
        BOT_MENTIONED (int): Bot mentioned in a message.
        MESSAGE_PINNED (int): Message pinned.
        MESSAGE_UNPINNED (int): Message unpinned.

        # Reactions
        REACTION_ADDED (int): Reaction added.
        REACTION_REMOVED (int): Reaction removed.

        # Users
        USER_JOINED (int): User joined the guild.
        USER_LEFT (int): User left the guild.
        USER_UPDATED (int): User updated their profile.

        # Members
        MEMBER_BANNED (int): Member banned from the guild.
        MEMBER_UNBANNED (int): Member unbanned from the guild.
        MEMBER_KICKED (int): Member kicked from the guild.
        MEMBER_UPDATED (int): Member updated their guild profile or roles.

        # Guilds
        GUILD_JOINED (int): Bot joined a guild.
        GUILD_LEFT (int): Bot left a guild.
        GUILD_UPDATED (int): Guild updated.

        # Channels
        CHANNEL_CREATED (int): Channel created.
        CHANNEL_UPDATED (int): Channel updated.
        CHANNEL_DELETED (int): Channel deleted.
        CHANNEL_OVERWRITES_UPDATED (int): Channel permission overwrites updated.
        VOICE_STATE_UPDATED (int): Voice state updated.

        # Categories
        CATEGORY_CREATED (int): Category created.
        CATEGORY_UPDATED (int): Category updated.
        CATEGORY_DELETED (int): Category deleted.

        # Roles
        ROLE_CREATED (int): Role created.
        ROLE_UPDATED (int): Role updated.
        ROLE_DELETED (int): Role deleted.
        ROLE_ASSIGNED (int): Role assigned to a member.
        ROLE_REMOVED (int): Role removed from a member.

        # Threads
        THREAD_CREATED (int): Thread created.
        THREAD_DELETED (int): Thread deleted.

        # Invites
        INVITE_CREATED (int): Invite created.
        INVITE_DELETED (int): Invite deleted.

        # Miscellaneous
        BUTTON_CLICKED (int): Button clicked.
        SELECT_MENU_USED (int): Select menu used.
    """

    # Messages
    MESSAGE_SENT: JDEEventType
    MESSAGE_EDITED: JDEEventType
    MESSAGE_DELETED: JDEEventType
    MESSAGE_BULK_DELETED: JDEEventType
    BOT_MENTIONED: JDEEventType
    MESSAGE_PINNED: JDEEventType
    MESSAGE_UNPINNED: JDEEventType

    # Reactions
    REACTION_ADDED: JDEEventType
    REACTION_REMOVED: JDEEventType

    # Users
    USER_JOINED: JDEEventType
    USER_LEFT: JDEEventType
    USER_UPDATED: JDEEventType

    # Members
    MEMBER_BANNED: JDEEventType
    MEMBER_UNBANNED: JDEEventType
    MEMBER_KICKED: JDEEventType
    MEMBER_UPDATED: JDEEventType

    # Guilds
    GUILD_JOINED: JDEEventType
    GUILD_LEFT: JDEEventType
    GUILD_UPDATED: JDEEventType

    # Channels
    CHANNEL_CREATED: JDEEventType
    CHANNEL_UPDATED: JDEEventType
    CHANNEL_DELETED: JDEEventType
    CHANNEL_OVERWRITES_UPDATED: JDEEventType
    VOICE_STATE_UPDATED: JDEEventType

    # Categories
    CATEGORY_CREATED: JDEEventType
    CATEGORY_UPDATED: JDEEventType
    CATEGORY_DELETED: JDEEventType

    # Roles
    ROLE_CREATED: JDEEventType
    ROLE_UPDATED: JDEEventType
    ROLE_DELETED: JDEEventType
    ROLE_ASSIGNED: JDEEventType
    ROLE_REMOVED: JDEEventType

    # Threads
    THREAD_CREATED: JDEEventType
    THREAD_DELETED: JDEEventType

    # Invites
    INVITE_CREATED: JDEEventType
    INVITE_DELETED: JDEEventType

    # Miscellaneous
    BUTTON_CLICKED: JDEEventType
    SELECT_MENU_USED: JDEEventType

__all__: Sequence[str] = [
    "JDEEventType",
]
