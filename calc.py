def calc():
    flag = True
    while flag:
        try:
            print('Enter any operation.\n'
                  'Enter "q" to quit.')
            data = input('> ').lower()
            if data == 'q':
                flag = False
                print('Process finished')
            if '**' in data:
                g = data.split('**')
                expo = int(g[0]) ** int(g[1])
                print(f'Exponentiation of {g[0]} to {g[1]} is: {expo}')
            elif '//' in data:
                e = data.split('//')
                int_divi = int(e[0]) // int(e[1])
                print(f'Integer division result of {e[0]} and {e[1]} is: {int_divi}')
            elif '+' in data:
                a = data.split('+')
                summ = int(a[0]) + int(a[1])
                print(f'Sum of {a[0]} and {a[1]} is: {summ}')
            elif '-' in data:
                b = data.split('-')
                diff = int(b[0]) - int(b[1])
                print(f'Difference between {b[0]} and {b[1]} is: {diff}')
            elif '*' in data:
                c = data.split('*')
                prod = int(c[0]) * int(c[1])
                print(f'Product of {c[0]} and {c[1]} is: {prod}')
            elif '/' in data:
                d = data.split('/')
                divi = int(d[0]) / int(d[1])
                print(f'Fraction of {d[0]} and {d[1]} is: {divi}')

            elif '%' in data:
                f = data.split('%')
                mod_divi = int(f[0]) % int(f[1])
                print(f'Modulo division result of {f[0]} and {f[1]} is: {mod_divi}')
        except ValueError:
            print('Enter a number, not a string!')
        except ZeroDivisionError:
            print('Number cannot be divided by 0!')


calc()
