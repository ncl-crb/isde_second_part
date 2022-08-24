
minutes_per_hour = 60

def create_time_slot():
    time = {
        'hours': None,
        'min': None
    }
    return time

def set_h_min(time, h, m):
    time['hours'] = h
    time['min'] = m
    return time


def set_min(time, m):
    h = int(m/minutes_per_hour)
    min = m - h * minutes_per_hour
    time['hours'] = h
    time['min'] = min
    return time


def get_h_min(time):
    print(f"{time['hours']} : {time['min']}")



def get_min(time):
    min = time['min'] + time['hours'] * minutes_per_hour
    print(f"{min}")



def main():
    time = create_time_slot()
    print(time)
    set_h_min(time, 1, 30)
    get_min(time)
    get_h_min(time)
    print("#############")
    set_min(time, 90)
    get_min(time)
    get_h_min(time)
    print("#############")
    set_min(time, 90)
    get_min(time)
    get_h_min(time)

if __name__ == '__main__':
    main()
