from .state import DOTState


def route_request(state: DOTState) -> DOTState:
    intent = state.get("intent", "unknown")

    if intent == "open_app":
        tool = "app_launcher"

    elif intent == "file_task":
        tool = "file_manager"

    elif intent == "web_task":
        tool = "browser"

    elif intent == "memory_task":
        tool = "memory"

    elif intent == "automation_task":
        tool = "scheduler"

    else:
        tool = "none"

    return {
        **state,
        "tool": tool,
    }