import random


def number_writer(strings: int, filename: str):
    with open(filename, 'w', encoding='utf-8') as f:
        for _ in range(strings):
            f.write(f'{random.randrange(-1000, 1000)}|{random.uniform(1000, -1000)}\n')



def main():
    number_writer(10, 'numbers.txt')


if __name__ == '__main__':
    main()
