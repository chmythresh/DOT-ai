from .state import DOTState


def detect_intent(user_input: str) -> str:
    text = user_input.lower().strip()

    if not text:
        return "unknown"

    if text.startswith(("open ", "launch ", "start ")):
        return "open_app"

    if any(word in text for word in ["file", "folder", "document"]):
        return "file_task"

    if any(word in text for word in ["search", "google", "find online", "browse"]):
        return "web_task"

    if any(word in text for word in ["remember", "remember this", "don't forget"]):
        return "memory_task"

    if any(word in text for word in ["remind me", "reminder", "schedule"]):
        return "automation_task"

    return "general_request"


def create_plan(state: DOTState) -> DOTState:
    user_input = state.get("user_input", "").strip()

    intent = detect_intent(user_input)

    if intent == "unknown":
        return {
            **state,
            "intent": "unknown",
            "plan": [],
        }

    plan = [user_input]

    return {
        **state,
        "intent": intent,
        "plan": plan,
    }


def create_response(state: DOTState) -> DOTState:
    user_input = state.get("user_input", "")
    intent = state.get("intent", "unknown")

    if intent == "unknown":
        response = "I didn't receive a request."

    elif intent == "open_app":
        response = f"I identified this as an app-opening request: {user_input}"

    elif intent == "file_task":
        response = f"I identified this as a file task: {user_input}"

    elif intent == "web_task":
        response = f"I identified this as a web task: {user_input}"

    elif intent == "memory_task":
        response = f"I identified this as a memory request: {user_input}"

    elif intent == "automation_task":
        response = f"I identified this as an automation request: {user_input}"

    else:
        response = f"I identified this as a general request: {user_input}"

    return {
        **state,
        "response": response,
    }