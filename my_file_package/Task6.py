import random
import string
from os import chdir
from pathlib import Path

def name_generator(min_length, max_length):
    while True:
        name_start = random.choice(string.ascii_uppercase) + random.choice('a' 'i' 'e' 'u' 'o')
        length = random.randint(min_length, max_length) - 2
        name_end = ''
        for _ in range(length):
            letter = random.choice(string.ascii_lowercase)
            name_end += letter
        name = name_start + name_end
        if not Path(name).is_file():
            return name


def file_creator(format: str, min_length=6, max_length=30, bites=256, file_count=42):
    for _ in range(file_count):
        print(Path.cwd())
        with open(f'{name_generator(min_length, max_length)}.{format}', 'bw', buffering=64) as f:
            bites = 256 if bites < 256 else 4096 if bites > 4096 else bites
            f.write(b'F' * bites)


def files_generator(path: str, *args):  # tuple of tuples with format and count
    if isinstance(path, str):
        path = Path(path)
    if not path.is_dir():
        path.mkdir(parents=True)
    chdir(path)
    for item in args:
        format = item[0]
        count = item[1]
        file_creator(format, file_count=count)


def main():
    files_generator(r'D:\Python projects\Advanced_python_course\Seminar_7\test_dir_for_task6', ('avi', 4), ('jpg', 3), ('mp3', 2))
__all__ = ['files_generator']

if __name__ == '__main__':
    main()
