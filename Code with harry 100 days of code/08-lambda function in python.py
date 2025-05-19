# #lambda functions are the single expressions


# def double(x):
#     return x*2

# print(double(5))


double = lambda x: x * 2
cube = lambda x: x**3


print(cube(5))


avg = lambda x, y: (x + y) / 2
print(avg(5, 6))


def appl(fx, value):
    return fx(value) + 6


print(appl(lambda x: x**3, 6))  # 216 + 6
