from math import sqrt


def dist(param, param1, points):
    x = points[param][0] - points[param1][0]
    y = points[param][1] - points[param1][1]
    x = x ** 2
    y = y ** 2
    return sqrt(x + y)
