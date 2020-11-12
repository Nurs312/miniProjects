def find_end(number):
    for num in range(1, number + 1):
        str_num = str(num)
        if 5 <= int(str_num) <= 20:
            print(f'{num} попыток.')
        elif str_num[-1] == '1':
            print(f'{num} попытка.')
        elif 1 < int(str_num[-1]) < 5:
            print(f'{num} попытки.')
        else:
            print(f'{num} попыток.')
find_end(100)