from tools.app_launcher import open_app
from tools.file_manager import list_directory, path_exists


TOOL_REGISTRY = {
    "app_launcher": open_app,
    "file_manager": list_directory,
    "path_exists": path_exists,
}


def get_tool(tool_name: str):
    return TOOL_REGISTRY.get(tool_name)


def list_tools():
    return list(TOOL_REGISTRY.keys())