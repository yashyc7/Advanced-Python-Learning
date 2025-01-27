# sets Unordered ,mutable , no duplicates


"""Creating the Set"""
myset = {"name", "apple", 2, 3, 1}
print(myset)

myset2 = set(["one", "two", "three"])
myset2 = set(("one", "two", "three"))
print(myset2)

myset3 = set("aaaabbbcccddddeeefff")
print(myset3)  # {'b', 'f', 'c', 'a', 'd', 'e'}
# since it stores the unique elements only

# Careful the empty set cannot be initialised with the {} , as this is interpreted as dict
# use the set() method instead

a = {}

print(type(a))  # <class 'dict'>
a = set()
print(type(a))  # <class 'set'>

"""Adding the elements in the set"""
my_set = set()
my_set.add(42)
my_set.add(True)
my_set.add("hello")

print(
    my_set
)  # Order doesn't matter here can be differ when printed {True, 42, 'hello'}


myset.add(42)  # nothing happens if the element is already present

print(my_set)  # {True, 42, 'hello'}


"""Remove Elements"""

# remove(x): removes x , raises a KeyError if element is not present

my_set = {"apple", "banana", "cherry"}
my_set.remove("apple")
print(my_set)

# keyError


# my_set.remove("orange") #since it doesnot exist
# since it would throw an key error


# to avoid the error throwing so the discard method doesn't throw error if the key is not found .

my_set.discard("cherry")
my_set.discard("blueberry")

# remove all elements

my_set.clear()
print(my_set)

# pop(): return and remove a random element

a = {True, 2, False, "hi", "hello"}

print(a.pop())

print(a)

"""Check if the elements is present in the set"""

my_set = {"apple", "banana", "cherrry"}


if "apple" in my_set:
    print("Yes")
else:
    print("no")
"""Union and Intersection"""

odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8, 10}
primes = {2, 3, 5, 7}

# union(): combine elements from both sets, no duplication

# note that this does not change the two sets

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)  # returns the empty set ()

i = evens.intersection(primes)
print(i)  # {2}

"""Difference of Sets"""

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

# difference(): returns a set with all the elements from the setA that are not in setB.
diff_set = setA.difference(setB)
print(diff_set)  # {4, 5, 6, 7, 8, 9}

# A.difference(B) is not the same as B.differnce(A)

diff_set = setB.difference(setA)
print(diff_set)  # {10, 11, 12}

# symmetric_difference(): returns a set with all the elements that are in setA and setB but not in both
diff_set = setA.symmetric_difference(setB)
print(diff_set)

# symmetric difference returns theose elements which are present in setA but not present in setB


"""Copying"""

set_org = {1, 2, 3, 4, 5}

set_copy = set_org

# now modifying the copy also affects the original
set_copy.update([3, 4, 5, 6, 7])
print(set_copy)
print(set_org)

# use copy() to actually copy the set
set_org = {1, 2, 3, 4, 5}
set_copy = set_org.copy()

# now modifying the copy does not affect the original
set_copy.update([3, 4, 5, 6, 7])
print(set_copy)
print(set_org)

"""Subset,Subset,and disjoint """
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
# issubset(setX): Returns True if setX contains the set
print(setA.issubset(setB))
print(setB.issubset(setA))  # True

# issuperset(setX): Returns True if the set contains setX
print(setA.issuperset(setB))  # True
print(setB.issuperset(setA))

# isdisjoint(setX) : Return True if both sets have a null intersection, i.e. no same elements
setC = {7, 8, 9}
print(setA.isdisjoint(setB))
print(setA.isdisjoint(setC))

"""Frozen set is just an immutable version of normal set. While elements of a set can be modified at any time, elements of frozen set remains the same after creation. Creation with: my_frozfrozensetenset = frozenset(iterable)"""
a = [0, 1, 2, 3, 4]

# The following is not allowed:
# a.add(5)
# a.remove(1)
# a.discard(1)
# a.clear()

# Also no update methods are allowed:
# a.update([1,2,3])

# Other set operations work
odds = frozenset({1, 3, 5, 7, 9})
evens = frozenset({0, 2, 4, 6, 8})
print(odds.union(evens))
print(odds.intersection(evens))
print(odds.difference(evens))
