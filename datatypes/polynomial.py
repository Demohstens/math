from function import _Funcion

class Polynomial(_Funcion):
    '''
    Class representing a polynomial function.
    Inherits: _Function

    Args:
        coefficients (list of touple (coefficient, exponent)): The coefficients of the polynomial function.
    '''

    #!Input format per coefficient: (coefficient, exponent)
    def __init__(self, *args) -> None:
        if isinstance(args[0], str):
            self._evaluate_string_function(args[0])
        for i, a in enumerate(args):
            setattr(self, "x" + str(i), a)

    def _evaluate_string_function(self, function):
        pass