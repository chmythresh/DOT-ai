from langgraph.graph import StateGraph, START, END

from .state import DOTState
from .planner import create_plan
from .router import route_request
from .tools import get_tool
from security.permissions import check_permission


def execute_tool(state: DOTState) -> DOTState:
    tool_name = state.get("tool", "none")

    if tool_name == "none":
        return {
            **state,
            "response": "No tool is required for this request.",
        }

    tool = get_tool(tool_name)

    if not check_permission(tool_name):
        return {
            **state,
            "response": f"Permission denied for tool: {tool_name}",
        }

    if tool is None:
        return {
            **state,
            "response": f"Tool '{tool_name}' is not available yet.",
        }

    if tool_name == "app_launcher":
        user_input = state.get("user_input", "")
        app_name = user_input

        for prefix in ["open ", "launch ", "start "]:
            if app_name.lower().startswith(prefix):
                app_name = app_name[len(prefix):]
                break

        result = tool(app_name)

        return {
            **state,
            "response": result,
        }

    if tool_name == "file_manager":
        user_input = state.get("user_input", "")

        path = "."

        for prefix in ["list files in ", "list folder ", "show files in "]:
            if user_input.lower().startswith(prefix):
                path = user_input[len(prefix):].strip()
                break

        result = tool(path)

        return {
            **state,
            "response": result,
        }

    return {
        **state,
        "response": "Tool execution is not implemented yet.",
    }


def build_graph():
    graph = StateGraph(DOTState)

    graph.add_node("planner", create_plan)
    graph.add_node("router", route_request)
    graph.add_node("execute", execute_tool)

    graph.add_edge(START, "planner")
    graph.add_edge("planner", "router")
    graph.add_edge("router", "execute")
    graph.add_edge("execute", END)

    return graph.compile()