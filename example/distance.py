from moon_utils import random_sample, pick_country
from cfg import csv_path
import math
from geopy.distance import geodesic


def find_shortest(cities_location):
    n = len(cities_location)
    print(cities_location)
    distance_min = 0
    distance_min_city = cities_location[0]
    for h in range(1, n):
        distance_min = distance_min + geodesic(cities_location[0], cities_location[h]).km
    for i in cities_location:
        cities_rest = cities_location.copy()
        cities_rest.remove(i)
        distance = 0
        for e in range(n - 1):
            distance = distance + geodesic(i, cities_rest[e]).km
        print("Sum of distance for ", i, "is: ", distance, 'km')
        if distance < distance_min:
            distance_min = distance
            distance_min_city = i
    return [distance_min_city, distance_min]
