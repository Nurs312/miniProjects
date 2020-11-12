def choco(part):
    def wrapper():
        print('Шоколад')
        part()
        print('Шоколад')

    return wrapper


def dough(part):
    def wrapper():
        print('Тесто')
        part()
        print('Тесто')

    return wrapper


@choco
@dough
def cream(filling='Крем'):
    print(filling)


cream()
