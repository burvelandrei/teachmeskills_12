class Bus:

    def __init__(self, speed: int, max_count_seats: int, max_speed: int, list_passengers_name: list, vakancy_flag: bool):
        self._speed = speed
        self._max_count_seats = max_count_seats
        self._max_speed = max_speed
        self._list_passengers_name = list_passengers_name
        self._vakancy_flag = vakancy_flag

    @property
    def speed(self):
        return self._speed

    @property
    def max_count_seats(self):
        return self._max_count_seats

    @property
    def max_speed(self):
        return self._max_speed

    @property
    def list_passengers_name(self):
        return self._list_passengers_name

    @property
    def vakancy_flag(self):
        return self._vakancy_flag

    def reduce_speed(self, value):
        self._speed = self._speed - value if self._speed - value > 0 else 0

    def increase_speed(self, value):
        self._speed = self._speed + value if self._speed + value < self._max_speed else self._max_speed

    def boarding_passengers(self, *args):
        if len(self._list_passengers_name) + len(args) <= self.max_count_seats:
            self._list_passengers_name += args
        self._vakancy_flag = True if len(self._list_passengers_name) < self._max_count_seats else False

    def disembarkation_of_passengers(self, *args):
        for name_passenger in args:
            self._list_passengers_name.remove(name_passenger)
        self._vakancy_flag = True if len(self._list_passengers_name) < self._max_count_seats else False

    def __iadd__(self, other):
        if len(self._list_passengers_name) < self._max_count_seats:
            self._list_passengers_name.append(other)
            self._vakancy_flag = True if len(self._list_passengers_name) < self._max_count_seats else False
            return self
        self._vakancy_flag = True if len(self._list_passengers_name) < self._max_count_seats else False
        return self

    def __isub__(self, other):
        self._list_passengers_name.remove(other)
        self._vakancy_flag = True if len(self._list_passengers_name) < self._max_count_seats else False
        return self

    def __contains__(self, other):
        return other in self._list_passengers_name




bus = Bus(45, 5, 100, ["Иванов", "Петров", "Смирнов", "Гришин"], True)
print("-" * 50)
bus.increase_speed(65)
print(bus.speed)
print("-" * 50)
bus.boarding_passengers("Бурвель", "Вакульчик")
print(bus.list_passengers_name)
print("-" * 50)
bus.disembarkation_of_passengers("Гришин", "Смирнов")
print(bus.list_passengers_name)
print("-" * 50)
bus += "Рыбин"
print(bus.list_passengers_name)
print("-" * 50)
bus -= "Иванов"
print(bus.list_passengers_name)
print("-" * 50)
print("Петров" in bus)
print("-" * 50)