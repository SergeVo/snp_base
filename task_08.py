# Написать метод multiply_numbers(inputs), который вернет произведение цифр,
# входящих в inputs.

def multiply_numbers(inputs=None):
    if inputs is None:
        return None

    str_inputs = str(inputs)

    result = 1
    is_digit = False

    for item in str_inputs:
        if item.isdigit():
            result *= int(item)
            is_digit = True

    if is_digit is True:
        return result


print(multiply_numbers())  # => None
print(multiply_numbers('ss'))  # => None
print(multiply_numbers('1234'))  # => 24
print(multiply_numbers('sssdd34'))  # => 12
print(multiply_numbers(2.3))  # => 6
print(multiply_numbers([5, 6, 4]))  # => 120
