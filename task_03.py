# Дан список элементов произвольной природы. Необходимо разработать метод
# max_odd(array), который определит максимальный нечетный элемент (21.000 = 21 и
# тоже считается нечетным элементом). Вернуть None, если таких элементов нет в
# переданном массиве.


def max_odd(array=None):
    if array is None:
        return None

    result = None
    for item in array:
        if isinstance(item, (int, float)):
            if item % 2 == 1:
                if result is None or item > result:
                    result = int(item)

    return result


print(max_odd([1, 2, 3, 4, 4]))                      # Ожидается: 3
print(max_odd([21.0, 2, 3, 4, 4]))                   # Ожидается: 21
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))    # Ожидается: 3
print(max_odd(['ololo', 'fufufu']))                   # Ожидается: None
print(max_odd([2, 2, 4, 8, 555]))
print(max_odd([]))
print(max_odd([23234, 2398798, 232342987, 87687621]))
print(max_odd(None))
