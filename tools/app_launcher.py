import shutil
import subprocess


APP_ALIASES = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "calc": "calc.exe",
    "paint": "mspaint.exe",
    "chrome": "chrome.exe",
    "edge": "msedge.exe",
    "wordpad": "write.exe",
}


def open_app(app_name: str) -> str:
    app_name = app_name.strip().lower()

    if not app_name:
        return "No application name was provided."

    executable = APP_ALIASES.get(app_name, app_name)

    # Check whether Windows can find the application.
    found_path = shutil.which(executable)

    if found_path:
        try:
            subprocess.Popen([found_path])
            return f"Opened {app_name}"
        except Exception as e:
            return f"Could not open {app_name}: {e}"

    # Try the executable directly.
    try:
        subprocess.Popen([executable])
        return f"Opened {app_name}"
    except FileNotFoundError:
        return f"Application not found: {app_name}"
    except Exception as e:
        return f"Could not open {app_name}: {e}"