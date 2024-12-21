
# Строки и индексация строк

# 1. В переменную example запишите любую строку.
example = "0123456789ABCDEF"

# 2. Выведите на экран(в консоль) первый символ этой строки.
print(example[0])

# 3. Выведите на экран(в консоль) последний символ этой строки (используя отрицательный индекс).
print(example[-1])

# 4. Выведите на экран(в консоль) вторую половину этой строки (С нечётным количеством символов: 'Urban' -> 'ban').
print(example[7:])

# 5. Выведите на экран(в консоль) это слово наоборот.
print(example[::-1])

# 6. Выведите на экран(в консоль) каждый второй символ этой строки. (Пример: 'Топинамбур'->'оиабр')
print(example[1::2])
