# Разработайте метод combine_anagrams(words_array), который принимает на вход
# массив слов и разбивает их в группы по анаграммам, регистр букв не имеет
# значения при определении анаграмм.

def combine_anagrams(words_array=None):
    if words_array is None:
        return None

    result = {}

    for word in words_array:
        sorted_word = ''.join(sorted(word))

        if sorted_word in result:
            result[sorted_word].append(word)
        else:
            result[sorted_word] = [word]

    return list(result.values())


print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar"]))
