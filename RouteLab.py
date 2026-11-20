import math

cities = [
    (12, 25),
    (48, 90),
    (70, 14),
    (20, 60),
    (83, 45),
    (52, 78),
    (5, 8),
    (91, 92)
]
'finds distance between two points'
def distance(a,b):
    return math.dist(a,b)
'finds the distance if you go from every city to the next in order of list and go back to start'
def routeLength(route):
    total = 0

    for i in range(len(route) - 1):
        total += distance(route[i], route[i + 1])
    total += distance(route[-1], route[0])

    return total
'starts at start, then goes to nearest, and then next closest, and then next closest, and so on'
def nearestNeighbor(start, cities):
    route = [start]
    unvisited = cities.copy()
    unvisited.remove(start)

    while unvisited:
        currentCity = route[-1]
        closestCity = None
        minDistance = float("inf")

        for city in unvisited:
            if distance(currentCity, city) < minDistance:
                minDistance = distance(currentCity, city)
                closestCity = city

        route.append(closestCity)
        unvisited.remove(closestCity)

    return route

'makes sure a route is valid'
def validateRoute(route, cities):
    if len(route) != len(cities):
        return False

    for city in route:
        if city not in cities:
            return False

        if route.count(city) > 1:
            return False

    return True


for city in cities:
    for i in range(len(cities)):
        closestSortMethod = nearestNeighbor(city, cities)
    print(f"distances: {routeLength(closestSortMethod)}")


def betterNearestNeighbor(cities):
    bestDistance = float("inf")
    bestRoute = []
    for city in cities:
        bestRoute = nearestNeighbor(city, cities)
        if routeLength(bestRoute) < bestDistance:
            bestDistance = routeLength(bestRoute)
            bestRoute = nearestNeighbor(city, cities)

    return(bestDistance)


print(betterNearestNeighbor(cities))