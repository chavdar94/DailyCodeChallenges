'''
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
'''


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    return pair(lambda a, b: a)


def cdr(pair):
    return pair(lambda a, b: b)


print(car(cons(112891382, 29)))
print(cdr(cons(5, 188)))
