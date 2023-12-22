def move_zeros(lst):
    zeros = []
    while 0 in lst:
        lst.remove(0)
        zeros.append(0)
    return lst + zeros


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
