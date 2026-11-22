

import subprocess
import sys

def check_dependencies():
    print("\n================================")
    print("       DEPENDENCY CHECKER")
    print("================================")

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "check"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print("All installed package dependencies are compatible.")
            print(result.stdout or "No dependency conflicts found.")
        else:
            print("Dependency issues found:")
            print(result.stdout)
            print(result.stderr)

    except Exception as error:
        print("Error checking dependencies:", error)


if __name__ == "__main__":
    check_dependencies()

