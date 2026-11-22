

import shutil
import subprocess

def check_compatibility():
    tools = ["git", "kicad-cli", "ngspice"]

    print("\n================================")
    print("      COMPATIBILITY CHECKER")
    print("================================")

    available = 0
    missing = 0

    for tool in tools:
        path = shutil.which(tool)

        if path:
            print(f"{tool}: Available")
            available += 1

            if tool == "git":
                command = [tool, "--version"]
            elif tool == "kicad-cli":
                command = [tool, "version"]
            else:
                command = [tool, "--version"]

            try:
                result = subprocess.run(
                    command,
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                output = result.stdout.strip() or result.stderr.strip()
                if output:
                    print("Version:", output.splitlines()[0])
            except Exception:
                print("Version information unavailable.")

        else:
            print(f"{tool}: Not found")
            missing += 1

    print("--------------------------------")
    print("Available tools:", available)
    print("Missing tools:", missing)
    print("================================")


if __name__ == "__main__":
    check_compatibility()


