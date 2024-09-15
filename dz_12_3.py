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

    def disembarkation_of_passengers(self, count_passengers):
        pass




bus = Bus(45, 10, 100, ["Иванов", "Петров", "Смирнов", "Гришин"], True)
bus.increase_speed(65)
print(bus.speed)