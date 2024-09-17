import os
import time
from pathlib import Path


def old_file_remover(path: Path, days: int):
    now = time.time()
    cut_off = now - (days * 86400)
    for root, dir_name, file_name in os.walk(path):
        for file in file_name:
            file_path = os.path.join(root, file)
            file_mod_time = os.path.getmtime(file_path)
            if file_mod_time < cut_off:
                os.remove(file_path)
                print(f'Deleted file: {file_path}')


if __name__ == '__main__':
    old_file_remover(Path('D:\Python projects\Advanced_python_course\HW_7\my_folder'), 0)
