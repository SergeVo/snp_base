# Необходимо разработать метод connect_dicts(dict1, dict2), который соединит 
# два переданных словаря, значениями ключей в которых являются числа, и вернет
# новый словарь, полученный по следующим правилам:
# • приоритетными являются ключи того словаря, сумма значений ключей
# которого больше (если суммы значений ключей будут равны, то второй
# словарь считается более приоритетным)
# • ключи со значениями меньше 10 не должны попасть в финальный
# словарь
# • получившийся словарь должен вернуться упорядоченным по значениям
# ключей в порядке возрастания.
# https://docs-python.ru/tutorial/operatsii-slovarjami-dict-python/filtr-kljuchej-znachenij-slovarja/

def connect_dicts(dict1=None, dict2=None):
    if dict1 is None or dict2 is None:
        return None

    sum_dict_1 = sum(dict1.values())
    sum_dict_2 = sum(dict2.values())

    if sum_dict_1 > sum_dict_2:
        max_dict = dict1
        min_dict = dict2
    elif sum_dict_1 == sum_dict_2:
        max_dict = dict2
        min_dict = dict1
    else:
        max_dict = dict2
        min_dict = dict1

    filtered_dictionary = {}

    for key, value in max_dict.items():
        if value > 10:
            filtered_dictionary[key] = value

    for key, value in min_dict.items():
        if value > 10 and key not in filtered_dictionary:
            filtered_dictionary[key] = value

    return dict(sorted(filtered_dictionary.items(), reverse=True))

print(connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 }))        # => { "c": 11, "b": 12 }
print(connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 })) # => { "d": 11, "c": 12, "a": 13 }
print(connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 }))      # => { "c": 11, "b": 12, "a": 15 }