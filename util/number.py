import math


def float_floor(number, point_num):
    return math.floor(number * (10 ** point_num)) / (10 ** point_num)
