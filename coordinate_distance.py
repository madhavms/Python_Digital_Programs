import math


def coordinate_distance(c1, c2):
    return math.dist(c1, c2)


m1 = [3, 2]
m2 = [9, 7]
print("Distance between the coordinates ({},{}) and ({},{}) is {}".format(m1[0],m1[1],m2[0],m2[1],coordinate_distance(m1, m2)))





