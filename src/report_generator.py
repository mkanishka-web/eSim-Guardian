
import os
from datetime import datetime
import json


def generate_report():

    project_path = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    report_folder = os.path.join(project_path, "reports")
    os.makedirs(report_folder, exist_ok=True)

    config_path = os.path.join(
        project_path, "config", "tools.json"
    )

    report_path = os.path.join(
        report_folder, "esim_guardian_report.txt"
    )

    try:
        with open(config_path, "r", encoding="utf-8-sig") as file:
            tools = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tools = {}

    with open(report_path, "w", encoding="utf-8") as file:

        file.write("====================================\n")
        file.write("          eSim GUARDIAN REPORT\n")
        file.write("====================================\n\n")

        file.write("Date and Time: ")
        file.write(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        file.write("\n\n")

        file.write("CONFIGURED TOOLS\n")
        file.write("----------------\n")

        for key, details in tools.items():
            file.write(
                details.get("name", key) + "\n"
            )
            file.write(
                "Required: "
                + str(details.get("required", False))
                + "\n\n"
            )

        file.write("AUDIT STATUS\n")
        file.write("------------\n")
        file.write("System scan: Run separately\n")
        file.write("Dependency check: Run separately\n")
        file.write("Compatibility check: Run separately\n")
        file.write("Health score: Not recorded in this report\n")

        file.write("\n====================================\n")
        file.write("       END OF REPORT\n")
        file.write("====================================\n")

    print("\nReport generated successfully!")
    print("Report location:", report_path)


if __name__ == "__main__":
    generate_report()
