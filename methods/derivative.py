def derive(f, times = 1):
    '''
    Derives a function f(x) and returns it as a new function.
    At this point i need to consider if I want polynomial functions to be written in LaTex or in a more readable format.
    '''
    "f'''(x) = 6x**6 + 2"

    if times == 0:
        return f
    

    
    while times > 0:
        return derive(f, times)