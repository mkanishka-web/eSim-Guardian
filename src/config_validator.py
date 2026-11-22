

from system_scanner import display_system_info
from dependency_checker import check_dependencies
from compatibility_checker import check_compatibility
from health_score import calculate_health_score


def main():
    while True:
        print("\n================================")
        print("          eSim GUARDIAN")
        print("    Smart Environment Auditor")
        print("================================")
        print("1. Scan System Information")
        print("2. Check Dependencies")
        print("3. Check Tool Compatibility")
        print("4. Calculate Health Score")
        print("5. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            display_system_info()

        elif choice == "2":
            check_dependencies()

        elif choice == "3":
            check_compatibility()

        elif choice == "4":
            calculate_health_score()

        elif choice == "5":
            print("Thank you for using eSim Guardian!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()



