# Реализуйте класс Dessert c геттерами и сеттерами name и calories,
# конструктором, принимающим на вход name и calories (не обязательные
# параметры), а также двумя # методами is_healthy (возвращает true при условии
# калорийности десерта менее 200) и is_delicious (возвращает true для всех
# десертов).

# class Dessert:

#     def __init__(self, name=None, calories=None):
#         self.name = name
#         self.calories = calories

#     def get_name(self):
#         return self.name

#     def get_calories(self):
#         return self.calories

#     def set_name(self, name):
#         self.name = name

#     def set_calories(self, calories):
#         self.calories = calories

#     def is_healthy(self):
#         return self.calories < 200

#     def is_delicious(self):
#         return True

#     def __str__(self):
#         return (f'Название: {self.name}; '
#                 f'Калории: {self.calories}; '
#                 f'Полезность: {self.is_healthy()}; '
#                 f'Вкусненько? {self.is_delicious()}.')
from task_11 import Dessert


class JellyBean(Dessert):
    def __init__(self, name=None, calories=None, flavour=None):
        super().__init__(name, calories)
        self.flavour = flavour

    def get_flavour(self):
        return self.flavour

    def set_flavour(self, flavour):
        self.flavour = flavour

    def is_delicious(self):
        return self.flavour != 'black licorice'

    def __str__(self):
        return (f'Название: {self.name}; '
                f'Калории: {self.calories}; '
                f'Вкус: {self.flavour}; '
                f'Полезность: {self.is_healthy()}; '
                f'Вкусненько? {self.is_delicious()}.')


# print(Dessert("Печенька", 500))
# print(Dessert("Арбуз", 100))
# print(Jellybean("Арбуз", 100, "black licorice"))
# print(Jellybean("Арбуз", 100, "просто сладкий"))
# print(Jellybean("Пиво", "сто", "какой надо вкус!"))
