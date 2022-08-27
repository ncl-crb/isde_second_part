def create_time_slot():
    time = {
        'hours': None,
        'min': None
    }
    return time


class TimeSlot:
    minutes_per_hour = 60

    def __init__(self, name='name', h=0, m=0):
        self.name = name
        self._h = h
        self._m = m

    @property
    def h(self):
        return self._h

    @property
    def m(self):
        return self._m

    @m.setter
    def m(self, m):
        self._h = int(m / self.minutes_per_hour)
        self._m = m % self.minutes_per_hour

    def set_h_m(self, h, m):
        self._h = h
        self._m = m

    def __add__(self, ts):
        new_time_slot = TimeSlot()
        new_time_slot.m = (self._h + ts._h * self.minutes_per_hour) + self._m +ts._m
        return new_time_slot


def main():
    t1 = TimeSlot('ciccio')
    t1.m = 20
    t2 = TimeSlot('ciccio1')
    t2.m = 30

    t_menu = t1 + t2
    print('t_menu = ', t_menu.h, t_menu.m)


if __name__ == '__main__':
    main()
