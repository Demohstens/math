
#More like calculus exceptions, but whatever.
class AlgebraicException(Exception):
    """Base class for all algebraic exceptions."""
    pass

class FunctionException(AlgebraicException):
    """Base class for all function exceptions."""
    pass

class CalculusException(Exception):
    """Base class for all calculus exceptions."""
    pass

class Test():
    def __init__(self, x):
        self.x = x
        self.x1 = self.x

new = Test(5)
new.x = 10
print(new.x1)