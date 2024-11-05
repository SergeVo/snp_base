# Дан список list и числовой диапазон range. Разработайте метод coincidence
# (list,range) для определения элементов из массива list, значения которого
# входят в указанный диапазон range. Если не передан хотя бы один из
# параметров, то  должен вернуться пустой массив.


def coincidence(list=None, range=None):
    if list is None or range is None:
        return []

    result = []

    for item in list:
        if isinstance(item, (int, float)) and range.start <= item < range.stop:
            result.append(item)

    return result


print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))
