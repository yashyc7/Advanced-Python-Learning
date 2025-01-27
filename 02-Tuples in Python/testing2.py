import timeit

print(
    timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000)
)  # takes more time to create the list /  0.17931300000054762
print(
    timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000)
)  # takes less time to create the tuple / 0.06579429999692366
