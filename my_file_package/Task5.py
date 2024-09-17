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


def file_creator(format: str, min_length=6, max_length=30, bites=256, file_count=42):
    for _ in range(file_count):
        with open(f'{name_generator(min_length, max_length)}.{format}', 'bw', buffering=64) as f:
            bites = 256 if bites < 256 else 4096 if bites > 4096 else bites
            f.write(b'F' * bites)


def files_generator(*args):  # tuple of tuples with format and count
    for item in args:
        format = item[0]
        count = item[1]
        file_creator(format, file_count=count)


def main():
    files_generator(('txt', 1), ('xml', 1), ('mp3', 2))


if __name__ == '__main__':
    main()

# seminar variant
# from random import randint, choices
# from string import ascii_lowercase, digits
#
#
# def create_files(
#         extension: str, min_name: int = 6, max_name: int = 30,
#         min_size: int = 256, max_size: int = 4096, count: int = 3
# ) -> None:
#     for _ in range(count):
#         name = "".join(choices(ascii_lowercase + "_" + digits, k=randint(min_name, max_name)))
#         data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
#         with open(f"{name}.{extension}", "wb") as f:
#             f.write(data)
#
#
# def gen_files(**kwargs) -> None:
#     # print(kwargs)
#     for ext, counter in kwargs.items():
#         create_files(extension=ext, count=counter)
#
#
# if __name__ == "__main__":
#     gen_files(bin=2, jpeg=1, txt=1)
