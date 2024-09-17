import zipfile
from pathlib import Path
import os



def dir_to_zip(path: Path, output_path: Path):
    with zipfile.ZipFile(output_path, 'w',zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, path))

if __name__ == '__main__':
    dir_to_zip(Path('D:\Python projects\Advanced_python_course\HW_7'), Path('D:\Python projects\Advanced_python_course\HW_7\my_folder'))