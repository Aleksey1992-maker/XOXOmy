# Инициализация карты
tabel = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

# Список победных линий
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]

# Вывод карты на экран
def print_tabel():
    print(tabel[0], end=" ")  #end=" "  - вводим для правильного расположения ячеек в ряд 1 2 3
    print(tabel[1], end=" ")
    print(tabel[2])

    print(tabel[3], end=" ")
    print(tabel[4], end=" ")
    print(tabel[5])

    print(tabel[6], end=" ")
    print(tabel[7], end=" ")
    print(tabel[8])


# Сделать ход в ячейку
def step_tabel(step, symbol):
    ind = tabel.index(step)
    tabel[ind] = symbol


# Получить текущий результат игры
def get_result():
    win = ""

    for i in victories:
        if tabel[i[0]] == "X" and tabel[i[1]] == "X" and tabel[i[2]] == "X":
            win = "X - крестики"
        if tabel[i[0]] == "O" and tabel[i[1]] == "O" and tabel[i[2]] == "O":
            win = "O - нолики"

    return win


# Основная программа
game_over = False
player1 = True

while game_over == False:

    # 1. Показываем карту
    print_tabel()

    # 2. Спросим у играющего куда делать ход
    if player1 == True:
        symbol = "X"
        step = int(input("Человек 1, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Человек 2, ваш ход: "))

    step_tabel(step, symbol)  # делаем ход в указанную ячейку
    win = get_result()  # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not (player1)

# Игра окончена. Покажем карту. Объявим победителя.
print_tabel()
print("Победил", win)