from ..datatypes.polynomial import Polynomial

def derive(f, times = 1):
    '''
    Derives a function f(x) and returns it as a new function.
    At this point i need to consider if I want polynomial functions to be written in LaTex or in a more readable format.
    '''
    "f(x) = {c : exp} {-c : exp}"

    if times == 0:
        return f
    
    for a in f.coefficients:
        if a[1] == 0:
            f.coefficients.remove(a)
        

    
    while times > 0:
        return derive(f, times)