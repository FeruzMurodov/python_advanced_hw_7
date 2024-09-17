import random
import string
from pathlib import Path


def name_generator():
    name_start = random.choice(string.ascii_uppercase) + random.choice(('a', 'i', 'e', 'u', 'o', 'y'))
    length = random.randint(4, 7) - 2
    name_end = ''
    for _ in range(length):
        letter = random.choice(string.ascii_lowercase)
        name_end += letter
    name = name_start + name_end
    return name


def name_saver(filename: str | Path, count: int):
    with open(filename, 'w', encoding='utf-8') as f:
        for _ in range(count):
            f.write(f'{name_generator()}\n')


def main():
    name_saver('names.txt', 15)


if __name__ == '__main__':
    main()


# seminar variant
# from random import randint, random.choice
# from pathlib import Path
#
# VOWELS = 'eyuioa'
# CONSONANTS = 'qwrtpsdfghjklzxcvbnm'
# MIN_LEN = 4
# MAX_LEN = 7
#
# def generate_names(filename: str | Path, names_count: int):
#     with open(filename, 'a', encoding='utf8') as f:
#         for _ in range(names_count):
#             name = ''
#             cur_letter = random.choice((-1, 1))
#             for _ in range(randint(MIN_LEN, MAX_LEN)):
#                 if cur_letter == -1:
#                     name += random.choice(VOWELS)
#                 else:
#                     name += random.choice(CONSONANTS)
#                 cur_letter *= -1
#         f.write(name.capitalize() + '\n')
#
# if __name__ == "__main__":
#     generate_names(Path('names.txt'), 10)

# seminar second variant
# def generate_names(filename: str | Path, names_count: int):
#     with open(filename, 'a', encoding='utf8') as f:
#         for _ in range(names_count):
#             cur_letter = random.choice((-1, 1))
#             name = ''.join(
#             random.choice(VOWELS) if (cur_letter:=cur_letter*(-1)) == -1 else random.choice(CONSONANTS) for _ in range(random.randint(MIN_LEN, MAX_LEN))
#     )
#     f.write(name.capitalize() + '\n')