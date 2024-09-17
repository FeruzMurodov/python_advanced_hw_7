# numbers_file = open('numbers.txt', 'r', encoding='utf-8')
# names_file = open('names.txt', 'r', encoding='utf-8')
# res_file = open('result_task3.txt', 'w+', encoding='utf-8')
#
# len_numbers = sum(1 for _ in numbers_file)
# len_names = sum(1 for _ in names_file)
# max_length = max(len_numbers, len_names)
# numbers_file.seek(0)
# names_file.seek(0)
#
# for i in range(10):
#     pair = numbers_file.readline().replace('\n', '').split('|')
#     number = round(int(pair[0]) * float(pair[1]), 2)
#     name = names_file.readline().replace('\n', '')
#     if number <= 0:
#         number = abs(number)
#         name = name.lower()
#     else:
#         number = round(number)
#         name = name.upper()
#     res_file.writelines(f'{name} - {number}\n')
#
# numbers_file.close()
# names_file.close()
# res_file.close()


# def numberds_file_reader(name: str):
#     numbers = []
#     with open(name, 'r', encoding='utf-8') as f:
#         for line in f:
#             pair = (line[:-1]).split('|')
#             numbers.append(round(int(pair[0]) * float(pair[1]), 2))
#     return numbers


# def names_file_reader(name: str):
#     names = []
#     with open(name, 'r', encoding='utf-8') as f:
#         for line in f:
#             names.append(line.replace('\n', ''))
#     return names


# seminar variant
from itertools import cycle


def join_file1_file2(filename1, filename2, result='file_new.txt'):
    with open(filename1, 'r', encoding='utf-8') as f_numbers, \
            open(filename2, 'r', encoding='utf-8') as f_names, \
            open(result, 'w', encoding='utf-8') as f_result:
        names = sum(1 for _ in f_names)
        numbers = sum(1 for _ in f_numbers)
        f_numbers.seek(0)
        f_names.seek(0)
        if names < numbers:
            for line1, line2 in zip(cycle(f_names.readlines()), f_numbers.readlines()):
                num1, num2 = map(float, line2.strip().split('|'))
                mult = num1 * num2
                if mult < 0:
                    f_result.write(f'{line1.lower()} - {-mult}\n')
                elif mult > 0:
                    f_result.write(f'{line1.upper()} - {round(mult)}\n')

        else:
            for line1, line2 in zip(f_names.readlines(), cycle(f_numbers.readlines())):
                num1, num2 = map(float, line2.strip().split('|'))
                mult = num1 * num2
                if mult < 0:
                    f_result.write(f'{line1.lower().strip()} - {-mult}\n')
                else:
                    f_result.write(f'{line1.upper().strip()} - {round(mult)}\n')


if __name__ == '__main__':
    join_file1_file2('numbers.txt', 'names.txt')
