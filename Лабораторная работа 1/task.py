# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
import math


class Product:
    """
    Класс, представляющий товар
    """
    def __init__(self, name: str, cost: int, count: int):
        """
        Создание и подготовка к работе объекта "Товар"
        :param name: Название товара
        :param cost: Объем стакана
        :param count: Количество товара

        Примеры:
        >>> product = Product("Хлеб", 100, 50)
        """
        if not isinstance(name, str):
            raise TypeError("Название товара должно быть типа str!")
        if not isinstance(cost, (int, float)):
            raise TypeError("Цена за товар должна быть типа int и float!")
        if cost <= 0:
            raise ValueError("Цена за товар должна быть числом больше 0!")
        if not isinstance(count, (int, float)):
            raise TypeError("Количество товара должна быть типа int и float!")
        if count <= 0:
            raise ValueError("Количество товара должно быть числом больше 0!")
        self.name = name
        self.cost = cost
        self.count = count

    def change_product_count(self, change) -> None:
        """
        Метод изменение количества товара
        :param change: Число, на которое нужно изменить количество товара.
        :raise ValueError: Если количество товара меньше чем число, на которое
        нужно изменить количество товара.

        Примеры:
        >>> product = Product("Хлеб", 100, 50)
        >>> product.change_product_count(10)
        """
        if not isinstance(change, int):
            raise TypeError("Число, на которое нужно изменить количество товара должно"
                            "быть типа int!")
        if self.count + change < 0:
            raise ValueError("Число, на которое нужно изменить количество товара"
                             "больше чем текущее количество товара")
        self.count += change

    def change_cost(self, new_cost: int) -> None:
        """
        Метод изменения цены товара
        :param new_cost: Новая цена товара
        :raise ValueError: Если цена товара меньше нуля

        Примеры:
        >>> product = Product("Хлеб", 100, 50)
        >>> product.change_cost(150)
        """
        if not isinstance(new_cost, (int, float)):
            raise TypeError("Новая цена товара должна иметь тип int или float!")
        if new_cost < 0:
            raise ValueError("Новая цена товара должна быть больше 0!")
        self.cost = new_cost


class Rectangle:
    """Класс, представляющий прямоугольник"""
    def __init__(self, first_side, second_side):
        """
        Создание и подготовка к работе объекта "Прямоугольник"
        :param first_side: Длина первой стороны
        :param second_side: Длина второй стороны

        Примеры:
        >>> rectangle = Rectangle(2, 4)
        """
        self.check_side(first_side)
        self.check_side(second_side)
        self.first_side = first_side
        self.second_side = second_side

    def check_side(self, value):
        """
        Метод проверки стороны на соответствие требованиям
        :param value: Длина стороны
        :raise ValueError: Если сторона меньше или равна нулю
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Сторона должна быть типа int или float!")
        if value <= 0:
            raise ValueError("Длина стороны должна быть больше 0!")

    def area(self) -> float:
        """
        Метод, подсчитывающий площадь прямоугольника
        :return: Площадь прямоугольника

        Примеры:
        >>> rectangle = Rectangle(3, 5)
        >>> rectangle.area()
        15
        """
        return self.first_side * self.second_side

    def perimeter(self) -> float:
        """
        Метод, подсчитывающий периметр прямоугольника
        :return: Периметр прямоугольника

        Примеры:
        >>> rectangle = Rectangle(3, 2)
        >>> rectangle.perimeter()
        10
        """
        return (self.first_side + self.second_side) * 2


class Vector:
    """Класс, представляющий вектор"""
    def __init__(self, x: float, y: float):
        """
        Создание и подготовка к работе объекта "Вектор"
        :param x: Координата вектора по x
        :param y: Координата вектора по y

        Примеры:
        >>> vector = Vector(2, 4)
        """
        self.x = self.check_coordinate(x)
        self.y = self.check_coordinate(y)

    def check_coordinate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Координата должна быть типа int или float!")
        return value

    def lenght(self) -> float:
        """
        Метод, вычисляющий длину вектора
        :return: Длину вектора

        Примеры:
        >>> vector = Vector(3, 4)
        >>> vector.lenght()
        5.0
        """
        return math.sqrt(self.x * self.x + self.y * self.y)

    def add(self, other_vector):
        """
        Метод, который прибавляет к текущему вектору другой
        :param other_vector: Другой вектор, типа Vector

        Примеры:
        >>> vector1 = Vector(2, 3)
        >>> vector2 = Vector(-2, 3)
        >>> vector1.add(vector2)
        """
        if not isinstance(other_vector, Vector):
            raise TypeError("Второй вектор должен быть типа Vector")
        self.x = self.x + other_vector.x
        self.y = self.y + other_vector.y


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
