

import os
import sys

# Add project root to Python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from src.system_scanner import scan_system
from src.dependency_checker import check_dependencies
from src.compatibility_checker import check_compatibility
from src.health_score import calculate_health
from src.report_generator import generate_report
from src.logger import log_info, log_error


def main():

    print("\n================================")
    print("          eSim GUARDIAN")
    print("    Smart Environment Auditor")
    print("================================")

    log_info("eSim Guardian started")

    while True:

        print("\n1. Scan System Information")
        print("2. Check Dependencies")
        print("3. Check Tool Compatibility")
        print("4. Calculate Health Score")
        print("5. Generate Report")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        try:

            if choice == "1":
                print("\nScanning system information...")
                result = scan_system()
                print(result)

            elif choice == "2":
                print("\nChecking dependencies...")
                result = check_dependencies()
                print(result)

            elif choice == "3":
                print("\nChecking tool compatibility...")
                result = check_compatibility()
                print(result)

            elif choice == "4":
                print("\nCalculating health score...")
                result = calculate_health()
                print("Health Score:", result)

            elif choice == "5":
                print("\nGenerating report...")
                result = generate_report()
                print(result)

            elif choice == "6":
                log_info("eSim Guardian closed")
                print("\nThank you for using eSim Guardian!")
                break

            else:
                print("\nInvalid choice! Please enter 1 to 6.")

        except Exception as e:
            log_error(str(e))
            print("\nAn error occurred:", e)


if __name__ == "__main__":
    main()
