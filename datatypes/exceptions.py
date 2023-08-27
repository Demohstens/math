
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