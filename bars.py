import json
from math import hypot
def load_data(filepath):
    with open(filepath) as json_file:
        bars_data=json_file.read()
    return json.loads(bars_data)


def get_biggest_bar(data):
    biggest=["",0]
    for bar in data:
        if bar['SeatsCount']>biggest[1]:
            biggest[1]=bar['SeatsCount']
            biggest[0]=bar['Name']
    return biggest


def get_smallest_bar(data):
    biggest = ["", 1000000]
    for bar in data:
        if bar['SeatsCount'] < biggest[1]:
            biggest[1] = bar['SeatsCount']
            biggest[0] = bar['Name']
    return biggest


def get_closest_bar(data, longitude, latitude):
    nearest = ["",1000000, None,None]
    for bar in data:
        bar_longitude=bar['geoData']['coordinates'][0]
        bar_latitude=bar['geoData']['coordinates'][1]
        distance=hypot(abs(longitude - bar_longitude) , abs(latitude - bar_latitude))
        if distance < nearest[1]:
            nearest[0] = bar['Name']
            nearest[1] = distance
            nearest[2] = bar_longitude
            nearest[3] = bar_latitude
    return nearest

if __name__ == '__main__':
    #filepath=input("Введите полное имя файла со списком баров (.json): ")
    filepath='data-2897-2016-11-23\data-2897-2016-11-23.json'
    bars_data=load_data(filepath)
    biggest_bar=get_biggest_bar(bars_data)
    print("Самый большой бар: " + biggest_bar[0] + " " + str(biggest_bar[1]) + " мест.")
    smallest_bar=get_smallest_bar(bars_data)
    print("Самый маленький бар: " + smallest_bar[0] + " " + str(smallest_bar[1]) + " мест.")
    my_longitude=float(input("Введите свою долготу: "))
    my_latitude=float(input("Введите свою широту: "))
    closest_bar=get_closest_bar(bars_data,my_longitude,my_latitude)
    print("Ближайший бар: " + closest_bar[0] + " координаты: " + str(closest_bar[3]) + ", " + str(closest_bar[2]))
    
