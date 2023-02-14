field = [[' '] * 3 for i in range(3)]


def show_field():
    rows = ['a', 'b', 'c']
    print('   1  2  3')
    for i in range(3):
        print(f'{rows[i]}  {"  ".join(field[i])}')


def inp_value():
    while True:
        values = ['a', 'b', 'c']
        r = input('По горизонтали: ')
        if r not in values:
            print('Неверное значение. Введите букву a, b или c.')
            continue
        break
    row = values.index(r)
    while True:
        c = input('По вертикали  : ')
        if not c.isnumeric() or int(c) not in range(1, 4):
            print('Неверное значение. Введите цифру 1, 2 или 3.')
            continue
        break
    column = int(c) - 1
    if field[row][column] != ' ':
        print('Эта ячейка занята. Выберите другую.')
        inp_value()
    else:
        return row, column


def winner(p):
    if field[0][0] == field[0][1] == field[0][2] == p or \
       field[1][0] == field[1][1] == field[1][2] == p or \
       field[2][0] == field[2][1] == field[2][2] == p or \
       field[0][0] == field[1][0] == field[2][0] == p or \
       field[0][1] == field[1][1] == field[2][1] == p or \
       field[0][2] == field[1][2] == field[2][2] == p or \
       field[0][0] == field[1][1] == field[2][2] == p or \
       field[0][2] == field[1][1] == field[2][0] == p:
        return True


show_field()

count = 1
while True:
    if count == 10:
        print('---')
        print('Ничья...')
        break
    if count % 2 != 0:
        player = 'X'
    else:
        player = '0'
    print('---')
    print(f'Ходит "{player}":')
    i, j = inp_value()
    field[i][j] = player
    if winner(player):
        print('')
        show_field()
        print('---')
        print(f'"{player}" выиграл!')
        break
    count += 1
    print('')
    show_field()
