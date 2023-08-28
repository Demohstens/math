def assert_attrs(f):
    def wrapper(self):
        if self.x1 != self.x:
            raise AttributeError("x1 is not equal to x")
        if self.x2 != self.y:
            raise AttributeError("x2 is not equal to y")
        return f(self)
    return wrapper