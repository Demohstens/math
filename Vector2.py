from Point import Point


class Vector2(Point):
    def __init__(self, x : float, y : float) -> None:
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return(f"({self.x}, {self.y})")
    
    def __add__(self, v):
        try:
            v[2]
        except IndexError:
            return Vector2(self.x + v[0], self.y + v[1])
        else:
            raise TypeError("Iterable superseeds max length for type 'Vector2'")
    
    #Allows for iterables to be used as "Makeshift" vectors. iterables longer than 2 raise a TypeError 
    def __sub__(self, v ):
        try:
            v[2]
        except IndexError:
            return Vector2(self.x - v[0], self.y - v[1])
        else:
            raise TypeError("Iterable superseeds max length for type 'Vector2'")
    #Problem: Strings

    def __mul__(self, v) -> super:
        v = float(v) #Makes isinstance shorter by not requiring the same test for ints
        if isinstance(v, float):
            return Vector2(self.x * v, self.y * v)
        elif isinstance(v, Vector2):
            return Vector2(self.x * v.x, self.y * v.y)
        else:
            raise AttributeError
        
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __bool__(self):
        if self.y and self.x:
            return True
        else:
            return False
        
    def __getitem__(self, index):
        match index:
            case 0:
                return self.x
            case "x":
                return self.x
            case 1:
                return self.y
            case "y":
                return self.y
            case -1:
                return self.y
            case _:
                raise IndexError 
    def create_function(self, origin = Point(0, 0)):
        m = self.y / self.x
        b = origin.y - (1 * m * origin.x)
        if abs(b) == 0:
            return f"f(x) = {m}x + 0"
        elif b > 0:
            return f"f(x) = {m}x +{b}"
        else:
            return f"f(x) = {m}x {b}"

def vector2(point , point2 = None):
    if point2:
        if isinstance(point, Point) and isinstance(point2, Point):
            return Vector2(point2.x - point.x, point2.y - point.y)
        else:
            return Vector2(point, point2)
    elif isinstance(point, Point):
        return Vector2(point.x, point.y)
    else:
        raise TypeError(f"{type(point)} is invalid type for type 'Vector2")
    
def create_function(vector, origin = Point(0, 0)):
    m = vector.y / vector.x
    b = origin.y - (1 * m * origin.x)
    if abs(b) == 0:
        return f"f(x) = {m}x + 0"
    elif b > 0:
        return f"f(x) = {m}x +{b}"
    else:
        return f"f(x) = {m}x {b}"