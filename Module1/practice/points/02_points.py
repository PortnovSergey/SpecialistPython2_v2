#!/usr/bin
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты

# TODO: your core here...

max = 0
zero_point = Point(0, 0)
for point in points:
    if max < point.dist(zero_point):
        max = point.dist(zero_point)

for point in points:
    if max == point.dist(zero_point):
        ret_point = point

print("Координаты наиболее удаленной точки = ", ret_point.x, ret_point.y )
