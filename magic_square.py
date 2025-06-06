n = int(input('Введите длинну стороны квадрата, а затем построчно через пробел его числа: '))
m = [[int(i) for i in input().split()] for _ in range(n)]
m2 = [i for r in m for i in r]  # Выпрямили матрицу, чтобы было проще проверить её числа
lm2 = len(m2)
l = [
        False] * lm2  # Список использованных чисел. Числа ставим в соответствие индексам. Те, числа что использованы будут вычеркиваться.
M = n * (n ** 2 + 1) / 2  # Найдем сразу магическое число, которому должна быть равна сумма рядов. См. википедию.


def mtest():
    # Проверка что используются только числа не превышающие n**2
    for i in m2:
        if 1 <= i <= lm2:
            l[i - 1] = True
        else:
            return 'NO'
    # Проверка, что использованы все числа от 1 до n**2
    for b in l:
        if not b:
            return 'NO'

    # Проверка сумм строк
    for r in m:
        if M != sum(r):
            return 'NO'

    # Проверка сумм столбцов
    for j in range(n):
        s = 0
        for i in range(n):
            s += m[i][j]
        if s != M:
            return 'NO'

    # Проверка сумы главной диагонали
    s = 0
    for i in range(n):
        s += m[i][i]
    if s != M:
        return 'NO'

    # Проверка суммы побочной диагонали
    s = 0
    for i in range(n):
        s += m[i][n - 1 - i]
    if s != M:
        return 'NO'

    return 'YES'


print(mtest())
