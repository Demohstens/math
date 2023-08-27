from exceptions import *
from point import Point
import math
'''
Implementation of a mathematical type function which takes an input and returns an output with respect to the input.
x -> f(x)
For Polynomial functions use the Polynomial subclass. Base class should not be used at all.
Naming convention off Wikipedia
'''

class _Function:
    """
    A class to represent a mathematical function.
    Should never be used on it's own. Use subclasses instead.

    Args:
        function (str or callable): The function, either as a string or as a function object.
        growth_rate (float, optional): The growth rate of the function. Defaults to 1.
        x_shift (float, optional): The horizontal shift of the function. Defaults to 0.
        y_shift (float, optional): The vertical shift of the function. Defaults to 0.
        degree (int, optional): The degree of the function. Defaults to None.
        type (str, optional): The type of the function. Defaults to None.
        x_intercept (float, optional): The x-intercept of the function. Defaults to None.
        y_intercept (float, optional): The y-intercept of the function. Defaults to None.
        points (list of type(Point) or of touple (x, y), optional): The points on the function. Defaults to None.
        roots (list of float, optional): The roots of the function. Defaults to None.
    """

    def __init__(self, **kwargs) -> None: 
        self.function = kwargs.get("function", None)
        self.growth_rate : float = kwargs.get("growth_rate", 1)
        self.x_shift : float = kwargs.get("x_shift", 0)
        self.y_shift : float = kwargs.get("y_shift", 0)
        self.degree  = kwargs.get("degree", None)
        self.type : str = kwargs.get("type", None)
        self.x_intercept : float = kwargs.get("x_intercept", None)
        self.y_intercept : float = kwargs.get("y_intercept", None)
        self.points : list = kwargs.get("points", None)
        self.point : Point = kwargs.get("point", None)
        self.roots : list = kwargs.get("roots", None)
        self._x : float = kwargs.get("x", 0)
        self._y : float = kwargs.get("y", None)


class LinearFunction(_Function):
    '''
    This class represents a linear function.

    Inherits: _Function
    
    Args:
        b (float): The growth rate of the function.
        c (float, optional): The vertical shift of the function. Defaults to 0.

    Methods:
        solve(solve_for): Solves for the given variable. Accepts "x", "y", and "c".
        
        get_point(point=None): Returns the first-best point on the function if possible. 
    
    '''

    def __init__(self, b, c = 0, **kwargs):
        super().__init__(**kwargs, type = "linear", degree = 1)
        #Check if input function is valid linear function
        if kwargs.get("type") != "linear":
            raise AlgebraicException("Cannot create a linear function with type other than 'linear'")
        if kwargs.get("degree") != 1:
            raise AlgebraicException("Cannot create a linear function with degree other than 1")
        #Parse the possible inputs for the function
        self.b : float = b.replace("x", "") or self.growth_rate
        #Assign c as either input or the super().y_shit. This will never be needed due to the default.
        self.c : float = c or self.growth_rate
    
    def get_point(self, point = None) -> Point:
        if point:
            if not point in self.points:
                self.points.append(point)
            return point
        elif self.points:
            return self.points[0]
        raise Exception("No Points?? Something went very wrong")
    
                
    def solve_for_y(self, x) -> float:
        return self.b * x + self.c

    def solve_for_x(self, y) -> float:
        if y == 0:
            raise ZeroDivisionError("Cannot solve for x when y is 0")
        return (y - self.c) / self.b
    
    def get_roots(self) -> list:
        for p in self.points:
            if p.y == 0:
                self.roots.append(p.x)
        return self.roots


class ConstantFunction(_Function):
    '''
    A class that represents a constant function

    inherits: _Function

    Args:
        c (float): The constant value of the function at each x value.
    '''
    def __init__(self, c : float, **kwargs) -> None:
        #As the degree and growth rate are always 0, they are not needed as inputs.
        super().__init__(**kwargs, type = "constant", degree = 0, growth_rate = 0, y_intersection = c)
        if self.growth_rate != 0:
            raise CalculusException("Cannot create a constant function with a growth rate other than 0") 
        if self.degree != 0:
            raise CalculusException("Cannot create a constant function with a degree other than 0")
        self.c = c or self.y_shift
        self.y = self.c
        if self.y != 0:
            self.roots = None
        else:
            self.roots = [-math.inf, math.inf]