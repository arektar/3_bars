import json
from math import hypot


def load_data(file_path):
    with open(file_path) as json_file:
        bars_data = json_file.read()
    return json.loads(bars_data)


def get_biggest_bar(data):
    biggest = max(data, key=lambda x: x['SeatsCount'])
    return biggest['Name'], biggest['SeatsCount']


def get_smallest_bar(data):
    smallest = min(data, key=lambda x: x['SeatsCount'])
    return smallest['Name'], smallest['SeatsCount']


def get_closest_bar(data, longitude, latitude):
    nearest = min(data, key=lambda x: hypot(
        abs(longitude - x['geoData']['coordinates'][0]), abs(latitude - x['geoData']['coordinates'][1])))
    return nearest['Name'], nearest['geoData']['coordinates'][0], nearest['geoData']['coordinates'][1]

if __name__ == '__main__':
    my_file_path = input("Введите полное имя файла со списком баров (.json): ")
    my_bars_data = load_data(my_file_path)
    biggest_bar = get_biggest_bar(my_bars_data)
    print("Самый большой бар: %s %d   мест." % (biggest_bar[0], biggest_bar[1]))
    smallest_bar = get_smallest_bar(my_bars_data)
    print("Самый маленький бар: %s %d мест." % (smallest_bar[0], smallest_bar[1]))
    my_longitude = float(input("Введите свою долготу: "))
    my_latitude = float(input("Введите свою широту: "))
    closest_bar = get_closest_bar(my_bars_data, my_longitude, my_latitude)
    print("Ближайший бар: %s координаты: %f, %f" % (closest_bar[0], closest_bar[2], closest_bar[1]))
