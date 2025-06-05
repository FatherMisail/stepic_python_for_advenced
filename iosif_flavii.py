buffer = []
buf_k = 0
buf_len = 0
buf_i = 0


def buffer_init(n, k):
    global buffer, buf_k, buf_len, buf_i

    buffer = [True] * n
    buf_k = k
    buf_len = len(buffer)
    buf_i = 0


def next(killer=False):
    global buf_i

    cnt = 1
    while cnt:
        buf_i += 1
        if buf_i == buf_len:
            buf_i = 0
        if buffer[buf_i]:
            cnt -= 1


def kill():
    global buffer
    buffer[buf_i] = False


def main():
    # n, k = 7, 5
    n, k = int(input('Укажите исходное количество человек в кругу: ')), int(input('Введите какой по счету выбывает: '))

    buffer_init(n, k)

    for _ in range(k - 1):
        next()
    kill()

    for _ in range(n - 2):
        for _ in range(k):
            next()
        kill()

    next()
    return buf_i + 1


print(f'Последний номер: {main()}')
