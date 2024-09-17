import os
from pathlib import Path


def search_by_extension(path: Path, extension: str):
    for dir_path, dir, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                print(f'{dir_path}\{file}')


def main():
    search_by_extension(Path(r'D:\Python projects\Advanced_python_course\HW_7\my_folder'), 'jpg')


if __name__ == '__main__':
    main()
