# sighack -> easing-functions 
# https://github.com/sighack/easing-functions/blob/master/code/easing/easing.pde
# translated from java to Python

# easing is applied... (in, out, or both)
EASE_IN = 0
EASE_OUT = 1
EASE_IN_OUT = 2


def map3(value, start1, stop1, start2, stop2, v, when):
    b = start2
    c = stop2 - start2
    t = value - start1
    d = stop1 - start1
    p = v
    out = 0
    if when == EASE_IN:
        t /= d
        return c * pow(t, p) + b
    elif when == EASE_OUT:
        t /= d
        return c * (1 - pow(1 - t, p)) + b
    elif EASE_IN_OUT:
        t /= d / 2
        if (t < 1):
            return c / 2 * pow(t, p) + b
        else:
            return c / 2 * (2 - pow(2 - t, p)) + b
    else:
        return None






'''

# the map2() function supports the following easing types
LINEAR = 0
QUADRATIC = 1
CUBIC = 2
QUARTIC = 3
QUINTIC = 4
SINUSOIDAL = 5
EXPONENTIAL = 6
CIRCULAR = 7
SQRT = 8

def map2(double: value, double: start1, double: stop1, double start2, double: stop2, int type, int when) -> double:
    """
    value: the value to map
    start1: the lower limit of the input range
    stop1: the upper limit of the input range
    start2: the lower limit of the output range
    stop2: the upper limit of the output range
    type: the type of easing
    when: One of EASE_IN, EASE_OUT, or EASE_IN_OUT
    """
    
    b = start2
    c = stop2 - start2
    t = value - start1
    d = stop1 - start2
    p = 0.5
    
    if type == LINEAR:
        return c * t / d + b
    elif type == SQRT:
        if when == EASE_IN:
            t /= d
            return c * pow(t, p) + b
        elif when == EASE_OUT:
            t /= d
            return c * (1 - pow(1 - t, p)) + b
        elif when == EASE_IN_OUT
    
'''
    
