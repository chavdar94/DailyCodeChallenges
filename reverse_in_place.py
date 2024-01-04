def reverse_in_place(lst):
    first = 0
    last = len(lst) - 1

    while first < last:
        lst[first], lst[last] = lst[last], lst[first]
        first += 1
        last -= 1

    print(' '.join(map(str, lst)))


# def reverse_in_place(lst):
#     for i in range(int(len(lst) / 2)):
#         temp = lst[i]
#         k = len(lst) - 1 - i
#         lst[i] = lst[k]
#         lst[k] = temp

#     print(lst)


reverse_in_place(['a', 'b', 'c', 'd', 'e'])
reverse_in_place([1, 2, 3, 4, 5])
