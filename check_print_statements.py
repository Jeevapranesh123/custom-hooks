import sys
import re


def check_for_prints(file_path):
    with open(file_path, "r") as file:
        if re.search(r"\bprint\(", file.read()):
            return True
    return False


def main():
    script_name = "check_print_statements.py"  # Name of this script
    files_checked = [
        f for f in sys.argv[1:] if not f.endswith(script_name)
    ]  # Exclude this script from the check
    failed_checks = []
    for file_path in files_checked:
        if file_path.endswith(".py") and check_for_prints(file_path):
            failed_checks.append(file_path)

    if failed_checks:
        print("Error: 'print' statements found in the following files:")
        for file in failed_checks:
            print(f"- {file}")
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
