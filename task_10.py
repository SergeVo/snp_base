# Разработайте функцию count_words(string), которая будет возвращать словарь со
# статистикой частоты употребления входящих в неё слов.

import re


def count_words(string=None):
    if string is None:
        return None

    string_lower = re.findall(r'[a-zа-яё]+', string.lower())

    counted_words = {}

    for word in string_lower:
        if word in counted_words:
            counted_words[word] += 1
        else:
            counted_words[word] = 1

    return counted_words


print(count_words("A man, a plan, a canal -- Panama"))
print(count_words("Doo bee doo bee doo"))
