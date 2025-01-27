import sys

mylist = [0, 1, 2, "hello", True]  #

mytuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(mylist), "bytes")
print(sys.getsizeof(mytuple), "bytes")
