from collections import defaultdict, deque

def find_minimum_roads(num_cities, num_roads, road_list):
    road_map = defaultdict(list)
    for city_a, city_b in road_list:
        road_map[city_a].append(city_b)
        road_map[city_b].append(city_a)

    visited_cities = [False] * (num_cities + 1)
    city_components = []

    def depth_first_search(city, component):
        stack = [city]
        while stack:
            current_city = stack.pop()
            if not visited_cities[current_city]:
                visited_cities[current_city] = True
                component.append(current_city)
                for neighbor in road_map[current_city]:
                    if not visited_cities[neighbor]:
                        stack.append(neighbor)

    for city in range(1, num_cities + 1):
        if not visited_cities[city]:
            component = []
            depth_first_search(city, component)
            city_components.append(component)

    if len(city_components) == 1:
        print(0)
        return

    required_roads = []
    for i in range(1, len(city_components)):
        required_roads.append((city_components[i - 1][0], city_components[i][0]))

    print(len(required_roads))
    for road in required_roads:
        print(road[0], road[1])

import sys
input = sys.stdin.read
data = input().splitlines()
num_cities, num_roads = map(int, data[0].split())
road_list = [tuple(map(int, line.split())) for line in data[1:]]

find_minimum_roads(num_cities, num_roads, road_list)