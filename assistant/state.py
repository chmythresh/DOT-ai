from typing import TypedDict


class DOTState(TypedDict, total=False):
    user_input: str
    intent: str
    plan: list[str]
    tool: str
    response: str