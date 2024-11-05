# Дан список целых чисел. Необходимо разработать метод sort_list(list),который
# поменяет местами все минимальные и максимальные элементы массива, а также
# добавит в конец массива одно минимальное значение из него.


def sort_list(lst=None):
    if lst is None or len(lst) == 0:
        return []

    if len(lst) == 1:
        return lst + [lst[0]]

    min_value = min(lst)
    max_value = max(lst)

    new_lst = lst[:]

    for i in range(len(new_lst)):
        if new_lst[i] == min_value:
            new_lst[i] = max_value
        elif new_lst[i] == max_value:
            new_lst[i] = min_value

    new_lst.append(min_value)

    return new_lst


print(sort_list([2, 4, 6, 8]))  # => [8, 4, 6, 2, 2]
print(sort_list([]))  # => []
print(sort_list([1]))  # => [1, 1]
print(sort_list([1, 2, 1, 3]))  # => [3, 2, 3, 1, 1]
