# Разработать метод date_in_future(integer), который вернет дату через integer дней.
# Если integer не является целым числом, то метод должен вывести текущую дату.
# Формат возвращаемой методом даты должен иметь следующий вид '01-01-2001
# 22:33:44’.

from datetime import datetime as dt, timedelta


def date_in_future(integer=None):
    if integer is None or not isinstance(integer, int):
        return dt.now().strftime('%d-%m-%Y %H:%M:%S')

    future_date_time = dt.now() + timedelta(days=integer)
    return future_date_time.strftime('%d-%m-%Y %H:%M:%S')


print(date_in_future(2))
print(date_in_future(0))
print(date_in_future(21))
