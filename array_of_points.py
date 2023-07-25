from Vector2 import Vector2, Point, vector2
from random import randrange

ps = []
vs = []
RAN = 250
for i in range(10):
    ps.append(Point(randrange(-RAN, RAN), randrange(-RAN, RAN)))

for i, p in enumerate(ps):
    if i < len(ps) - 1:
        vector = vector2(p, ps[i+1])
        vs.append(vector)
