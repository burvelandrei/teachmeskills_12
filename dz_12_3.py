class Bus:
    """
    Класс описывающий Автобус. Имеет атрибуты скорости,
    максимальной вместимости, максимальной скорости, список
    фамилий пассажиров и словарь мест.
    Реализованы методы изменения скорости(сбросить/добавить),
    посадки/высадки пассажиров, посадки/высадки пассажира по фамилии,
    проверка на присутствие пассажира в автобусе
    """

    def __init__(self, max_count_seats: int, max_speed: int):
        self._speed = 0
        self._max_count_seats = max_count_seats
        self._max_speed = max_speed
        self._list_passengers_name = []
        self._vakancy_flag = True
        self._dict_of_seats = {key: None for key in range(1, max_count_seats + 1)}

    @property
    def speed(self):
        return self._speed

    @property
    def list_passengers_name(self):
        return self._list_passengers_name

    def reduce_speed(self, value):
        self._speed = self._speed - value if self._speed - value > 0 else 0

    def increase_speed(self, value):
        self._speed = (
            self._speed + value
            if self._speed + value < self._max_speed
            else self._max_speed
        )

    def boarding_passengers(self, *args):
        for passenger in args:
            if len(self._list_passengers_name) < self._max_count_seats:
                for seat, value in self._dict_of_seats.items():
                    if value is None:
                        self._dict_of_seats[seat] = passenger
                        self._list_passengers_name.append(passenger)
                        break
            else:
                self._vakancy_flag = False
                print("В автобусе нет мест!")
                break

    def disembarkation_of_passengers(self, *args):
        for passenger in args:
            for seat, value in self._dict_of_seats.items():
                if value == passenger:
                    self._dict_of_seats[seat] = None
                    self._list_passengers_name.remove(passenger)
        self._vakancy_flag = (
            True if len(self._list_passengers_name) < self._max_count_seats else False
        )

    def __iadd__(self, other):
        if len(self._list_passengers_name) < self._max_count_seats:
            for seat, value in self._dict_of_seats.items():
                if value is None:
                    self._dict_of_seats[seat] = other
                    self._list_passengers_name.append(other)
            return self
        print("В автобусе нет мест!")
        self._vakancy_flag = (
            True if len(self._list_passengers_name) < self._max_count_seats else False
        )
        return self

    def __isub__(self, other):
        for seat, value in self._dict_of_seats.items():
            if value == other:
                self._dict_of_seats[seat] = None
                self._list_passengers_name.remove(other)
        self._vakancy_flag = (
            True if len(self._list_passengers_name) < self._max_count_seats else False
        )
        return self

    def __contains__(self, other):
        return other in self._list_passengers_name

    def __str__(self) -> str:
        return f"{self._speed}|{self._list_passengers_name}|{self._dict_of_seats}"


bus = Bus(3, 100)
print("-" * 50)
bus.increase_speed(65)
print(bus.speed)
print("-" * 50)
bus.reduce_speed(15)
print(bus.speed)
print("-" * 50)
bus.boarding_passengers("Бурвель", "Вакульчик", "Иванов")
print(bus.list_passengers_name)
print("-" * 50)
bus.disembarkation_of_passengers("Вакульчик")
print(bus.list_passengers_name)
print("-" * 50)
bus += "Рыбин"
print(bus.list_passengers_name)
print("-" * 50)
bus -= "Бурвель"
print(bus.list_passengers_name)
print("-" * 50)
print("Петров" in bus)
print("-" * 50)
print(bus)
