"""
Практика с дескрипторами, путём создания класса человека с именем, возрастом и последующим изменением его возраста
"""


class Info:
    """
    Дескриптор с сеттером для утсановки локальной перемнной, вывода значения в переменной
    и сеттером для установки значения
    """
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class Person:
    """
    Формируем дескрипторы
    """
    name = Info()
    old = Info()
    weight = Info()

    def __init__(self, name, old, weight):
        """
        Используем дескрипторы
        """
        self.name = name
        self.old = old
        self.weight = weight
        self.verif(name, old, weight)

    @classmethod
    def verif(cls, name, old, weight):
        """
        Проверяем входные данные
        """
        if type(name) != str:
            raise TypeError("Имя должно быть строкой")
        if name.isdigit():
            raise TypeError("В имени не могут присутствовать числа")
        if type(old) != int:
            raise TypeError("Возраст должен быть целым числом")
        if type(weight) != float:
            raise TypeError("Вес должен быть вещественным числом")



if __name__ == "__main__":
    people = Person('Маквэрик', 23, 83.0)
    print(people.old)
    hb = people.old = 24
    print('После 07.10.2023 мне уже будет:' + str(hb))
