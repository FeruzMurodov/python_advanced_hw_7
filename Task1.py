from itertools import count
from pathlib import Path
from my_file_package import Task6
import os


def file_renamer(path: Path, old_name_range: list, new_suffix: str, digits_count: int, org_extension: str,
                 new_extension):
    file_counter = 0
    for file in path.iterdir():
        if file.is_file() and file.suffix == org_extension:
            file_name = file.name
            new_name = f'{file_name[old_name_range[0]:old_name_range[1]]}{new_suffix}{file_counter}.{new_extension}'
            os.rename(file, new_name)
            file_counter += 1




def main():
    #Task6.files_generator(r'D:\Python projects\Advanced_python_course\HW_7\my_folder', ('avi', 3), ('jpg', 3),('mp3', 3))
    file_renamer(Path(r'D:\Python projects\Advanced_python_course\HW_7'), [0, 3], 'NEW', 2, '.png', 'bin', )


if __name__ == '__main__':
    main()
