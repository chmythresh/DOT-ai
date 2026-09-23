SENSITIVE_TOOLS = {
    "delete_file",
    "write_file",
    "move_file",
    "system_control",
}


def requires_permission(tool_name: str) -> bool:
    return tool_name in SENSITIVE_TOOLS


def check_permission(tool_name: str) -> bool:
    if not requires_permission(tool_name):
        return True

    answer = input(
        f"DOT wants to use '{tool_name}'. "
        "Do you allow this? (yes/no): "
    )

    return answer.strip().lower() in ["yes", "y"]