def cube(x):
    return x**3


print(cube(2))


l = [1, 2, 3, 5, 6, 3, 5]
# wanted to convert this list into the cube of these items

newl = list(map(cube, l))  # takes the function and the iterable


print(newl)


# filter method is used for filtering the data

filter_function = lambda x: x > 4

new_l2 = list(filter(filter_function, l))

print(new_l2)

# now reduce function


from functools import reduce


numbers = [1, 2, 3, 4, 5]

print(reduce(lambda x, y: x + y, numbers))
