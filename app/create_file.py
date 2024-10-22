import sys
import os
from datetime import datetime


def create_directory(path: str) -> None:
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Directory '{path}' created!")
    except OSError as e:
        print(f"Error creating directory: {e}")
        sys.exit(1)


def create_file(file_path: str) -> None:
    if os.path.exists(file_path):
        print(f"File '{file_path}' exists. Appending new content...")
    else:
        print(f"Creating new file: '{file_path}'")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as f:
        f.write(f"\n{timestamp}\n")

        count = 1
        while True:
            content = input(f"Enter content line {count}: ")
            if content.lower() == "stop":
                break
            f.write(f"{count} {content}\n")
            count += 1


def main() -> None:
    args = sys.argv[1:]

    if "-d" in args:
        d_index = args.index("-d")
        dir_parts = args[d_index + 1:]
        if "-f" in dir_parts:
            f_index = dir_parts.index("-f")
            dir_parts = dir_parts[:f_index]
        directory_path = os.path.join(*dir_parts)
        create_directory(directory_path)

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
        if "-d" in args:
            directory_path = os.path.join(*args[args.index("-d") + 1:f_index])
            file_path = os.path.join(directory_path, file_name)
        else:
            file_path = file_name

        create_file(file_path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Arguments Error!")
    else:
        main()
