# JarDiscordEngine — Event System Specifications

## 1. Objective

Create a dedicated event system inside JarDiscordEngine.

The system must provide three main capabilities:

1. **Event definitions:** identify the events supported by JDE.
2. **Event subscriptions:** allow developers to register callbacks for event types.
3. **Event conditions:** allow developers to filter events before callbacks execute.

The system must remain independent of Pycord as much as possible.

Pycord receives Discord events; JDE converts them into its own entities and event context, evaluates conditions, and dispatches callbacks.

This architecture should also allow future custom JDE events without exposing Pycord's event API.

---

## 2. Package structure

The proposed structure follows the current JarDiscordEngine package organization:

```text
events/
├── __init__.py
├── context.py
├── enums.py
├── conditions.py
├── decorators.py
├── subscription.py
├── events.py
├── dispatcher.py
└── tmp.md
```

### Module responsibilities

| Module | Responsibility |
|---|---|
| `context.py` | Defines `JDEEventContext`. |
| `enums.py` | Defines event types and event-related enumerations. |
| `conditions.py` | Defines built-in event conditions and their evaluation. |
| `decorators.py` | Provides event and condition decorators. |
| `subscription.py` | Defines the representation of a registered callback. |
| `events.py` | Implements the public `JDEEvents` interface. |
| `dispatcher.py` | Handles internal event dispatching and callback execution. |

### Public and internal classes

The main public class should be:

- `JDEEvents`: the event system exposed to developers through a bot instance.

Other public classes and types:

- `JDEEventContext`
- `JDEEventType`
- `JDEEventSubscription`
- Condition classes, if exposing them is useful for custom conditions.

Internal implementation classes should only be introduced when they provide a meaningful shared responsibility.

Potential internal classes:

- `_JDEEventDispatcher`: handles callback dispatching and execution.
- `_JDEEventCondition`: common base for built-in conditions, if inheritance is useful.
- `_JDEEventConditionRegistry`: stores and validates available condition types, if the condition system becomes sufficiently complex.

These are implementation suggestions, not mandatory classes. Avoid creating internal classes for simple operations that can remain functions.

---

## 3. Event types

Start with the following event categories.

### Messages

- `MESSAGE_SENT`
- `MESSAGE_EDITED`
- `MESSAGE_DELETED`
- `MESSAGE_BULK_DELETED`
- `BOT_MENTIONED`
- `MESSAGE_PINNED`
- `MESSAGE_UNPINNED`

### Reactions

- `REACTION_ADDED`
- `REACTION_REMOVED`

### Members and users

- `USER_JOINED`
- `USER_LEFT`
- `USER_UPDATED`
- `MEMBER_BANNED`
- `MEMBER_UNBANNED`
- `MEMBER_KICKED`
- `MEMBER_UPDATED`

### Guilds

- `GUILD_JOINED`
- `GUILD_LEFT`
- `GUILD_UPDATED`

### Channels and categories

- `CHANNEL_CREATED`
- `CHANNEL_UPDATED`
- `CHANNEL_DELETED`
- `CATEGORY_CREATED`
- `CATEGORY_UPDATED`
- `CATEGORY_DELETED`
- `CHANNEL_OVERWRITES_UPDATED`
- `VOICE_STATE_UPDATED`

### Roles

- `ROLE_CREATED`
- `ROLE_UPDATED`
- `ROLE_DELETED`
- `ROLE_ASSIGNED`
- `ROLE_REMOVED`

### Threads

- `THREAD_CREATED`
- `THREAD_DELETED`

### Invites

- `INVITE_CREATED`
- `INVITE_DELETED`

### Miscellaneous

- `BUTTON_CLICKED`
- `SELECT_MENU_USED`

Not every event is necessarily available directly through a Discord gateway event. For example, identifying a kick may require audit-log correlation and additional permissions.

Only expose events when their detection mechanism is sufficiently reliable.

### Derived events

Some JDE events should be derived from other events.

For example, `BOT_MENTIONED` should be generated when JDE receives a message containing a mention of the bot.

`MESSAGE_SENT` should include messages authored by bots unless explicitly filtered by the developer.

---

## 4. Event context

Every callback should receive a single `JDEEventContext` object.

This avoids passing numerous separate arguments and provides a consistent interface across event types.

### Proposed properties

| Property | Type | Purpose |
|---|---|---|
| `event_type` | `JDEEventType` | Event being dispatched. |
| `timestamp` | `datetime` | Time at which JDE received the event. |
| `guild` | `JDEEntityGuild \| None` | Related guild. |
| `channel` | Appropriate JDE channel entity or `None` | Related channel, including private channels if supported. |
| `category` | `JDEEntityGuildCategory \| None` | Related category. |
| `user` | `JDEEntityUser \| None` | User responsible for or associated with the event. |
| `target_user` | `JDEEntityUser \| None` | User affected by the event. |
| `member` | Guild-member entity or `None` | Guild-specific user information, if available. |
| `message` | `JDEEntityMessage \| None` | Related message. |
| `before_message` | `JDEEntityMessage \| None` | Message state before an edit. |
| `reaction` | JDE emoji entity or `None` | Emoji involved in a reaction event. |
| `role` | `JDEEntityRole \| None` | Related role. |
| `reason` | `str \| None` | Moderation reason, when available. |
| `data` | `dict[str, object]` | Additional event-specific information. |

Additional before-state properties may be introduced when needed:

- `channel_before`
- `category_before`
- `role_before`

The context should only contain information relevant to the event. Unavailable properties should remain `None`.

**Important:** `user` and `target_user` must remain distinct. For example, during a moderation action, `user` represents the moderator and `target_user` represents the affected member.

The exact entity annotations must be adapted to the entities available in JDE. In particular, private channels must not be silently discarded because the current channel type only represents guild channels.

---

## 5. Event registration

The public interface should be accessible through:

```python
bot.events
```

Developers should be able to register callbacks using decorators or explicit registration.

### Decorator registration

```python
@JDE.Events.event(JDEEventType.MESSAGE_SENT)
async def on_message(context: JDEEventContext) -> None:
    ...
```

### Explicit registration

```python
async def on_message(context: JDEEventContext) -> None:
    ...


bot.events.register(
    JDEEventType.MESSAGE_SENT,
    on_message,
)
```

Both approaches must create the same type of event subscription.

### Decorator behavior

The `@event()` decorator should attach registration metadata to the callback rather than immediately registering it in a global registry.

The bot's event system should discover and register decorated callbacks when their module or extension is loaded.

This avoids mixing callbacks belonging to different bot instances and makes multiple bot instances possible.

---

## 6. Event conditions

Conditions allow developers to filter events without repeatedly implementing the same checks inside callbacks.

They should be declarative and independent of Pycord.

Conditions should operate exclusively on `JDEEventContext` and JDE entities.

### Condition naming

Condition names should describe the predicate being evaluated.

The API must not be restricted to `do_*`.

Possible naming families include:

| Prefix | Meaning | Examples |
|---|---|---|
| `do_*` | Checks whether something happens or matches a value. | `do_contain`, `do_equal`, `do_start_with` |
| `is_*` | Checks a property or state. | `is_bot`, `is_dm`, `is_owner` |
| `has_*` | Checks whether something is present or possessed. | `has_role`, `has_attachment`, `has_permission` |
| `can_*` | Checks whether an action or capability is allowed. | `can_manage_messages`, `can_moderate` |
| Other | Conditions that need a more specific name. | `matches`, `condition` |

These are naming conventions, not separate condition systems.

### Proposed built-in conditions

**Message conditions**

- `do_contain()`
- `do_not_contain()`
- `do_equal()`
- `do_start_with()`
- `do_end_with()`
- `do_match()` — regular expression matching.
- `has_attachment()`
- `has_embed()`
- `has_mention()`

**User and member conditions**

- `is_bot()`
- `is_not_bot()`
- `is_owner()`
- `is_member()`
- `has_role()`
- `has_permission()`

**Guild and channel conditions**

- `is_dm()`
- `is_guild()`
- `is_nsfw()`
- `is_thread()`
- `do_guild()`
- `do_channel()`
- `do_category()`

**General conditions**

- `do_user()`
- `do_mention()`
- `do_role()`
- Custom conditions through a generic condition decorator.

The list can grow as JDE's entity and permission systems develop.

### Matching modes

String-based conditions should support:

- `mode="any"`: at least one supplied value must match.
- `mode="all"`: every supplied value must match.

They should also support:

- `case_sensitive=False` by default.
- `case_sensitive=True` for case-sensitive matching.

Example:

```python
@JDE.Events.event(JDEEventType.MESSAGE_SENT)
@JDE.Events.do_contain(
    "hi",
    "hello",
    "heya",
    mode="any",
    case_sensitive=False,
)
async def on_message(context: JDEEventContext) -> None:
    ...
```

### Custom conditions

Developers should be able to define their own synchronous or asynchronous conditions.

Conceptual API:

```python
@JDE.Events.condition
async def has_permission(context: JDEEventContext) -> bool:
    return await check_permission(context.user)
```

The condition system must support both regular functions and coroutines.

### Event-aware validation

Conditions must declare which event contexts they require.

For example, a message-content condition cannot be attached to `CHANNEL_CREATED`.

This incompatibility should raise a dedicated `JDEEventConditionError` during registration instead of silently returning `False` at runtime.

Conditions should be represented by identifiable condition objects or metadata, rather than anonymous lambdas alone. This allows JDE to validate compatibility before dispatching events.

---

## 7. Event subscriptions

Introduce `JDEEventSubscription` to represent a registered callback.

It should contain at least:

- `event_type`
- `callback`
- `conditions`

The subscription should be the common representation used by both decorator-based and explicit registration.

It may later support:

- Enabled/disabled state.
- Execution priority.
- One-time execution.
- Subscription identifiers.
- Registration source (module or extension).
- Execution statistics.

These additional features are not required for the initial implementation.

---

## 8. Event dispatching

The event lifecycle should follow this sequence:

```text
Discord / Pycord event
        |
        v
JDE event adapter
        |
        v
JDE entity conversion
        |
        v
JDEEventContext
        |
        v
JDE event dispatcher
        |
        v
Find matching subscriptions
        |
        v
Validate/evaluate conditions
        |
        v
Execute matching callbacks
```

For example, when Pycord receives `on_message`:

1. JDE converts the relevant Discord objects into JDE entities.
2. JDE creates a `JDEEventContext`.
3. JDE dispatches `MESSAGE_SENT`.
4. The dispatcher finds all matching subscriptions.
5. Their conditions are evaluated.
6. Callbacks whose conditions pass are executed.

A single Discord event may trigger multiple JDE events or callbacks when appropriate.

### Execution behavior

Initial behavior should follow these rules:

- Callbacks execute sequentially in registration order.
- One callback failing must not prevent other callbacks from executing.
- Exceptions are caught and logged with the callback and event information.
- Synchronous and asynchronous conditions are supported.
- Asynchronous callbacks are awaited.
- Bot-authored messages are dispatched; developers can filter them using conditions.

Concurrent callback execution and timeouts can be considered later.

---

## 9. Public API examples

### Message filtering

```python
@JDE.Events.event(JDEEventType.MESSAGE_SENT)
@JDE.Events.do_contain("hi", "hello", mode="any")
@JDE.Events.is_not_bot()
async def hello_reaction(context: JDEEventContext) -> None:
    if context.message is None:
        return

    await context.message.reply("Hello!")
```

### Bot mention

```python
@JDE.Events.event(JDEEventType.BOT_MENTIONED)
@JDE.Events.is_not_bot()
async def bot_mentioned(context: JDEEventContext) -> None:
    if context.message is None:
        return

    await context.message.reply("You called?")
```

### Channel creation

```python
@JDE.Events.event(JDEEventType.CHANNEL_CREATED)
async def channel_created(context: JDEEventContext) -> None:
    if context.channel is None:
        return

    print(f"New channel: {context.channel.name}")
```

These examples describe the intended API. Actual method names and entity behavior must follow the existing JDE implementation.

---

## 10. Important design decisions

The following decisions should guide implementation.

| Topic | Initial decision |
|---|---|
| Multiple bot instances | Each bot owns its own `JDEEvents` instance. |
| Callback registration | Decorators attach metadata; explicit registration is also supported. |
| Conditions | Conditions operate on `JDEEventContext`, never directly on Pycord objects. |
| Callback execution | Sequential by default. |
| Callback failures | Isolated and logged; other callbacks continue. |
| Async conditions | Supported. |
| Bot messages | Dispatched by default. |
| Direct messages | Supported through an appropriate common/private channel entity. |
| Custom events | Architecture should allow JDE-defined events in addition to Discord events. |
| Condition validation | Incompatible conditions raise an exception during registration. |

---

## 11. Exceptions

Event-specific exceptions should be introduced only where they provide meaningful error handling.

Initially, consider:

- `JDEEventError`: base exception for event-system errors.
- `JDEEventRegistrationError`: invalid or duplicate registration.
- `JDEEventConditionError`: invalid or incompatible condition.

These can be added to the existing JDE exception conventions rather than introducing an unnecessarily complex exception hierarchy.

---

## 12. Implementation order

Develop the system incrementally.

### Phase 1 — Core infrastructure

- `JDEEventType`
- `JDEEventContext`
- `JDEEventSubscription`
- `JDEEvents`
- `_JDEEventDispatcher`

### Phase 2 — Registration

- `@event()` decorator.
- Explicit registration.
- Decorated callback discovery.
- Duplicate registration handling.
- Multiple bot instance isolation.

### Phase 3 — Discord integration

Initially support:

- `MESSAGE_SENT`
- `MESSAGE_EDITED`
- `MESSAGE_DELETED`
- `CHANNEL_CREATED`
- `BOT_MENTIONED`

Ensure that Discord objects are converted into the appropriate JDE entities before dispatch.

### Phase 4 — Conditions

Implement:

- Message matching conditions.
- User and member conditions.
- Guild and channel conditions.
- Custom synchronous conditions.
- Custom asynchronous conditions.
- Event-aware condition validation.

### Phase 5 — Reliability and testing

Test:

- Multiple callbacks for the same event.
- Multiple bot instances.
- Callback exceptions.
- Invalid registrations.
- Incompatible conditions.
- Synchronous and asynchronous conditions.
- Bot-authored messages.
- Direct messages.
- Missing or unavailable context properties.

### Phase 6 — Additional event coverage

Expand to reactions, members, roles, voice, threads, invites, and interactions.

Only add events once their Discord integration and detection behavior are sufficiently reliable.

---

## 13. Final architectural direction

The event system should have one main public entry point: `JDEEvents`.

`JDEEventContext` provides a standardized payload, `JDEEventSubscription` represents registered callbacks, and `_JDEEventDispatcher` handles execution internally.

Conditions should be reusable, event-aware, and extensible. Their naming should describe their actual purpose rather than forcing every condition into a `do_*` convention.

Most importantly, **do not introduce internal classes simply to hide implementation details**. Internal classes should exist when they provide shared functionality, state management, or a meaningful architectural responsibility.

The initial implementation should prioritize a reliable core, message and channel integration, and a flexible condition system. The broader event catalogue can be implemented progressively.