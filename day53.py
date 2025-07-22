# # MAP ,FILETER, REDUCE


# def square(l):
#     return l**2

# # for i in a:
# #     newi.append(square(i))

# a = [1, 2, 3, 4, 5]

# new = list(map(lambda x: x**2, a))
# print(new)  

# # FILTER
# def filter_function(x):
#     return x < 4
    
# b = list(filter(filter_function,a))
# print(b)

# # REDUCE

# import functools
# from functools import reduce

# c = [1, 2, 3, 4, 5]
# # d = reduce(lambda x, y: x + y, c)

# def sum(s,t):
#     return s+t

# d = reduce(sum, c)
# print(d)


# practice ------------------------------------------------------------------

def cube(n):
    return n**3
a = [1, 2, 3, 4, 5]
new = list(map(cube, a))