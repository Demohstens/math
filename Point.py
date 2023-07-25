class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return (f"Point at ({self.x}|{self.y})")
                    
    def add_y(self, y):
        self.y += y
    def add_x(self, x):
        self.x += x
    def copy(self):
        return Point(self.x, self.y)
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    def __add__(self, point : super):
        self.x += point.x
        self.y += point.y