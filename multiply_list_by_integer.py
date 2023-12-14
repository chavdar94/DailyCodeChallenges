'''
Given a list of integers l, return the list with each value multiplied by integer n.

Restrictions:
The code must not:

contain *.
use eval() or exec()
contain for
modify l
Happy coding :)
'''


def multiply(n, l):
    return list(map((n).__mul__, l))


print(multiply(2, [1, 2, 3, 4]))
