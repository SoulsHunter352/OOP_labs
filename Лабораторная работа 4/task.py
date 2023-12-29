from typing import Union


class Plane:
    """Класс, представляющий самолёт"""
    def __init__(self, name: str, empty_weight: Union[int, float], engine_power: Union[int, float],
                 tank_volume: Union[int, float],
                 current_amount_of_fuel: Union[int, float]) -> None:
        """
        Создание и подготовка объекта "Самолет"
        :param name: Наименование самолета (Устанавливается при создании объекта)
        :param empty_weight: Масса пустого самолета (кг.) (На параметр накладываются ограничения, поэтому protected)
        :param engine_power: Тяга двигателя (кгс.) (На параметр накладываются ограничения, поэтому protected)
        :param tank_volume: Вместимость топливного бака (кг.) (Устанавливается при создании объекта, не изменяется)
        :param current_amount_of_fuel: Текущее количество топлива (кг.) (На параметр накладываются ограничения, поэтому
            protected)
        """
        if not isinstance(name, str):
            raise TypeError("Наименование самолета должно быть типа str!")
        self._name = name
        self.empty_weight = empty_weight
        self.engine_power = engine_power
        if not isinstance(tank_volume, (int, float)):
            raise TypeError("Объем бака самолета должен быть типа int или str!")
        if tank_volume <= 0:
            raise ValueError("Объём бака самолета должен быть числом больше нуля!")
        self._tank_volume = tank_volume
        self.current_amount_of_fuel = current_amount_of_fuel

    @property
    def name(self) -> str:
        return self._name

    @property
    def engine_power(self) -> Union[int, float]:
        return self._engine_power

    @engine_power.setter
    def engine_power(self, new_engine_power) -> None:
        if not isinstance(new_engine_power, (int, float)):
            raise TypeError("Мощность двигателя должна быть типа int или float!")
        if new_engine_power <= 0:
            raise ValueError("Мощность двигателя должна быть числом больше нуля!")
        self._engine_power = new_engine_power

    @property
    def empty_weight(self) -> Union[int, float]:
        return self._empty_weight

    @empty_weight.setter
    def empty_weight(self, new_empty_weight: Union[int, float]) -> None:
        if not isinstance(new_empty_weight, (int, float)):
            raise TypeError("Масса пустого самолета должна быть типа int или float!")
        if new_empty_weight <= 0:
            raise ValueError("Масса пустого самолета должна быть числом больше 0!")
        self._empty_weight = new_empty_weight

    @property
    def tank_volume(self) -> Union[int, float]:
        return self._tank_volume

    @property
    def current_amount_of_fuel(self) -> Union[int, float]:
        return self._current_amount_of_fuel

    @current_amount_of_fuel.setter
    def current_amount_of_fuel(self, new_amount_of_fuel) -> None:
        if not isinstance(new_amount_of_fuel, (int, float)):
            raise TypeError("Текущее количество топлива должно быть типа int или float!")
        if new_amount_of_fuel < 0:
            raise ValueError("Текущее количество топлива не должно быть меньше нуля!")
        elif new_amount_of_fuel > self.tank_volume:
            raise ValueError("Текущее количество топлива не должно превышать вместимость бака!")
        self._current_amount_of_fuel = new_amount_of_fuel

    def check_flight_readiness(self) -> bool:
        """
        Метод проверки готовности самолета к полету
        :return: Готов или не готов
        """
        if self.current_amount_of_fuel > 0:
            print("Самолет готов к полёту.")
            return True
        else:
            print("Самолет не готов к полету! Недостаточно топлива!")
            return False

    def equip_plane(self) -> None:
        """
        Метод полной экипировки самолета
        """
        self.current_amount_of_fuel = self.tank_volume
        print("Самолет полностью укомплектован для полета")

    def __str__(self) -> str:
        return f"Наименование самолета: '{self.name}'. Мощность: {self.engine_power} кгс. " \
               f"Текущее количество топлива: {self.current_amount_of_fuel} кг. " \
               f"Масса самолета с учетом топлива: {self.empty_weight + self.current_amount_of_fuel} кг."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, empty_weight={self.empty_weight}, " \
               f"engine_power={self.engine_power}, tank_volume={self.tank_volume}, " \
               f"current_amount_of_fuel={self.current_amount_of_fuel})"


class Fighter(Plane):
    """Класс, представляющий истребитель"""
    def __init__(self, name: str, empty_weight: Union[int, float], engine_power: Union[int, float],
                 tank_volume: Union[int, float], current_amount_of_fuel: Union[int, float], rockets_name: str,
                 max_rockets_cnt: int, current_rockets_count: int):
        """
        Создание и подготовка объекта "Истребитель"
        :param name: Наименование самолета (Устанавливается при создании объекта)
        :param empty_weight: Масса пустого самолета (кг.) (На параметр накладываются ограничения, поэтому protected)
        :param engine_power: Тяга двигателя (кгс.) (На параметр накладываются ограничения, поэтому protected)
        :param tank_volume: Вместимость топливного бака (кг.) (Устанавливается при создании объекта, не изменяется)
        :param current_amount_of_fuel: Текущее количество топлива (кг.) (На параметр накладываются ограничения, поэтому
            protected)
        :param rockets_name: Наименование ракет (Устанавливается при создании объекта, не изменяется)
        :param max_rockets_cnt: Максимальное количество ракет (Устанавливается при создании объекта, не изменяется)
        :param current_rockets_count: Текущее количество ракет (На параметр накладываются ограничения,
            поэтому protected)
        """
        super().__init__(name, empty_weight, engine_power, tank_volume, current_amount_of_fuel)
        if not isinstance(rockets_name, str):
            raise TypeError("Название ракет должно быть типа str!")
        if not isinstance(max_rockets_cnt, int):
            raise TypeError("Максимальное количество ракет должно быть типа int!")
        if max_rockets_cnt <= 0:
            raise ValueError("Максимальное количество ракет должно быть числом больше нуля!")
        self._rockets_name = rockets_name
        self._max_rockets_cnt = max_rockets_cnt
        self.current_rockets_count = current_rockets_count

    @property
    def rockets_name(self) -> str:
        return self._rockets_name

    @property
    def max_rockets_cnt(self) -> int:
        return self._max_rockets_cnt

    @property
    def current_rockets_count(self) -> int:
        return self._current_rockets_count

    @current_rockets_count.setter
    def current_rockets_count(self, new_current_rockets_count: int) -> None:
        if not isinstance(new_current_rockets_count, int):
            raise TypeError("Текущее количество ракет должно быть типа int!")
        if new_current_rockets_count < 0:
            raise ValueError("Текущее количество ракет должно быть числом больше или равным нулю!")
        if new_current_rockets_count > self.max_rockets_cnt:
            raise ValueError("Текущее количество ракет не должно быть больше "
                             "максимально допустимого числа ракет!")
        self._current_rockets_count = new_current_rockets_count

    def equip_plane(self) -> None:
        # Перегружаем метод, так как нужно заполнить самолет ракетами
        """
        Метод экипировки самолета
        Заправка и снаряжение ракетами
        """
        self.current_amount_of_fuel = self.tank_volume
        self.current_rockets_count = self.max_rockets_cnt

    def __str__(self) -> str:
        # Перегружаем, так как для истребителя важно вооружение на борту
        return f"Наименование самолета: '{self.name}'. Мощность: {self.engine_power}. " \
               f"Текущее количество топлива: {self.current_amount_of_fuel} кг. " \
               f"Масса самолета с учетом топлива: {self.empty_weight + self.current_amount_of_fuel} кг. " \
               f"Вооружение: {self.rockets_name!r} в количестве {self.current_rockets_count} шт."

    def __repr__(self):
        # Перегружаем метод, так как появились новые параметры при создании объекта
        return f"{self.__class__.__name__}(name={self.name!r}, empty_weight={self.empty_weight}, " \
               f"engine_power={self.engine_power}, tank_volume={self.tank_volume}, " \
               f"current_amount_of_fuel={self.current_amount_of_fuel}, rockets_name={self._rockets_name!r}, " \
               f"max_rockets_cnt={self.max_rockets_cnt}, current_rockets_count={self.current_rockets_count})"


class Passenger(Plane):
    """Класс, представляющий пассажирский самолет"""
    def __init__(self, name: str, empty_weight: Union[int, float], engine_power: Union[int, float],
                 tank_volume: Union[int, float], current_amount_of_fuel: Union[int, float],
                 max_passenger_count: int, current_passengers_count: int):
        """
        Создание и подготовка объекта "Пассажирский самолёт"
        :param name: Наименование самолета (Устанавливается при создании объекта)
        :param empty_weight: Масса пустого самолета (кг.) (На параметр накладываются ограничения, поэтому protected)
        :param engine_power: Тяга двигателя (кгс.) (На параметр накладываются ограничения, поэтому protected)
        :param tank_volume: Вместимость топливного бака (кг.) (Устанавливается при создании объекта, не изменяется)
        :param current_amount_of_fuel: Текущее количество топлива (кг.) (На параметр накладываются ограничения, поэтому
            protected)
        :param max_passenger_count: Максимальное количество пассажиров (чел.) (Устанавливается при создании объекта,
            не изменяется)
        :param current_passengers_count: Текущее число пассажиров (чел.) (На параметр накладываются ограничения,
            поэтому protected)
        """
        super().__init__(name, empty_weight, engine_power, tank_volume, current_amount_of_fuel)
        if not isinstance(max_passenger_count, int):
            raise TypeError("Максимальное число пассажиров должно быть типа int!")
        if max_passenger_count <= 0:
            raise ValueError("Максимальное число пассажиров должно быть числом больше 0!")
        self._max_passenger_count = max_passenger_count
        self.current_passengers_count = current_passengers_count

    @property
    def max_passengers_count(self) -> int:
        return self._max_passenger_count

    @property
    def current_passengers_count(self) -> int:
        return self._current_passengers_count

    @current_passengers_count.setter
    def current_passengers_count(self, new_current_passenger_count: int) -> None:
        if not isinstance(new_current_passenger_count, int):
            raise TypeError("Текущее число пассажиров должно быть типа int!")
        if new_current_passenger_count < 0:
            raise ValueError("Текущее число пассажиров должно быть числом больше 0!")
        elif new_current_passenger_count > self.max_passengers_count:
            raise ValueError("Текущее число пассажиров не может быть больше максимального числа пассажиров!")
        self._current_passengers_count = new_current_passenger_count

    def equip_plane(self) -> None:
        # Перегружаем метод, так как нужно заполнить самолет пассажирами
        """
        Метод экипировки самолета.
        Заправляет самолет и заполняет его пассажирами
        """
        self.current_amount_of_fuel = self.tank_volume
        self.current_passengers_count = self.max_passengers_count
        print("Самолёт полностью укомплектован!")

    def __str__(self) -> str:
        # Перегружаем, так как для пассажирского самолета важно количество пассажиров
        return f"Наименование самолета: '{self.name}'. Мощность: {self.engine_power} кгс. " \
               f"Текущее количество топлива: {self.current_amount_of_fuel} кг. " \
               f"Масса самолета с учетом топлива: {self.empty_weight + self.current_amount_of_fuel} кг. " \
               f"Текущее число пассажиров: {self.current_passengers_count} чел."

    def __repr__(self) -> str:
        # Перегружаем метод, так как появились новые параметры при создании объекта
        return f"{self.__class__.__name__}(name={self.name!r}, empty_weight={self.empty_weight}, " \
               f"engine_power={self.engine_power}, tank_volume={self.tank_volume}, " \
               f"current_amount_of_fuel={self.current_amount_of_fuel}, " \
               f"max_passenger_count={self.max_passengers_count}, " \
               f"current_passengers_count={self.current_passengers_count})"


if __name__ == "__main__":
    # Write your solution here
    # pass
    plane1 = Plane("Боинг", 1000.0, 2500, 20000, 0)
    print(plane1)
    print(repr(plane1))
    fighter1 = Fighter("Су-25", 500, 1000, 2000, 100, "Воздух-воздух", 4, 2)
    fighter1.current_rockets_count -= 2
    print(fighter1)
    print(repr(fighter1))
    print(fighter1.check_flight_readiness())
    fighter1.equip_plane()
    print(fighter1)
    passenger = Passenger("Airbus-A310", 150, 4000, 2000, 100.2, 205, 100)
    print(passenger)
    print(repr(passenger))
    passenger.equip_plane()
    print(passenger)
    print(repr(passenger))
