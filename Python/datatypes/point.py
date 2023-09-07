from misc import assert_attrs

class Coordinate:
    '''
    Abstract class representing a coordinate in 2, or n-dimensional space.
    '''
    def __init__(self, *args) -> None:
        if args:
            for i, n in enumerate(args):
                setattr(self, "x" + str(i +1), n)

class Point(Coordinate):
    '''
    Class representing a point in 2D space.
    Args:
        x1 (float): The x coordinate of the point.
        x2 (float): The y coordinate of the point.
    '''
    def __init__(self, x1, x2) -> None:
        self.x1 = x1
        self.x2 = x2
        self.x = x1
        self.y = x2
        self.last = (x1, x2)

    @assert_attrs
    def __str__(self) -> str:
        return (f"Point at ({self.x1}|{self.x2})")
    
    def add_y(self, x2):
        self.x2 += x2
    def add_x(self, x1):
        self.x1 += x1

        
    def copy(self):
        return Point(self.x1, self.x2)
    def __abs__(self):
        return (self.x1 ** 2 + self.x2 ** 2) ** 0.5
    def __add__(self, point):
        self.x1 += point.x1
        self.x2 += point.x2

new = Point(1, 2)
print(new)
