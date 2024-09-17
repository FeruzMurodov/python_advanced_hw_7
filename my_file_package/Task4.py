import random
import string


def name_generator(min_length, max_length):
    name_start = random.choice(string.ascii_uppercase) + random.choice('a' 'i' 'e' 'u' 'o')
    length = random.randint(min_length, max_length) - 2
    name_end = ''
    for _ in range(length):
        letter = random.choice(string.ascii_lowercase)
        name_end += letter
    name = name_start + name_end
    return name


def file_creator(format: str, min_length: int = 6, max_length: int = 30, bites=256, file_count=3):
    for _ in range(file_count):
        with open(f'{name_generator(min_length, max_length)}.{format}', 'bw', buffering=64) as f:
            bites = 256 if bites < 256 else 4096 if bites > 4096 else bites
            f.write(b'F' * bites)


def main():
    file_creator('bin', min_length=3, max_length=6, bites=300, file_count=1)


if __name__ == '__main__':
    main()
