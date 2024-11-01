# Разработайте метод is_palindrome(string), который будет определять, является ли
# параметр string палиндромом (строкой, которая читается одинаково как сначала
# так и с конца), при условии игнорирования пробелов, знаков препинания и
# регистра.

def is_palindrome(string):
    if string is None:
        return False

    if isinstance(string, (int, float)):
        string = str(string)

    chars = []

    for char in string.lower():
        if char.isalnum():
            chars.append(char)

    print(string, chars)
    return chars == chars[::-1]


print(is_palindrome("A man, a plan, a canal -- Panama"))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome(333))
print(is_palindrome(None))
print(is_palindrome("Abracadabra"))
