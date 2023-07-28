from Vector2 import Vector2, Point, vector2
from random import randrange

def create_vs(number_of_points = 50, RAN = 250):
    ps = []
    vs = []
    for i in range(number_of_points):
        ps.append(Point(randrange(-RAN, RAN), randrange(-RAN, RAN)))

    for i, p in enumerate(ps):
        if i < len(ps) - 1:
            vector = vector2(p, ps[i+1])
            vs.append(vector)
    return vs