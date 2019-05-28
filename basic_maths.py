def add(*args):
    s  = 0
    for i in args:
        s += i
    return s

def difference(a, b):
    return a - b

def multiply(*args):
    p  = 0
    for i in args:
        p *= i
    return p

def divide(a,b):
    return a/b

def remainder(a,b):
    return a%b

def mod(a):
    if a >=0:
        return a
    else:
        return -a

def signum(a):
    return mod(a)/a
