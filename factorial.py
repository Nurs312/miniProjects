num = int(input("Enter any number and I'll show you it's factorial: "))
factorial = 1
for x in range(1, num + 1):
    factorial *= x
print(f'Factorial of "{num}" is "{factorial}".')
