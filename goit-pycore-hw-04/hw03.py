import sys
from pathlib import Path
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def print_directory_tree(path: Path, prefix=""):
    if not path.exists():
        print(Fore.RED + f"Error: Path '{path}' does not exist.")
        return
    if not path.is_dir():
        print(Fore.RED + f"Error: Path '{path}' is not a directory.")
        return

    for item in sorted(path.iterdir()):
        if item.is_dir():
            print(prefix + Fore.BLUE + f"📂 {item.name}")
            print_directory_tree(item, prefix + "    ")
        else:
            print(prefix + Fore.GREEN + f"📜 {item.name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(Fore.RED + "Usage: python hw04.py <path_to_directory>")
    else:
        directory_path = Path(sys.argv[1])
        print(Fore.YELLOW + f"📦 {directory_path.name}")
        print_directory_tree(directory_path)
