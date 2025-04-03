from collections import Counter

"""A counter is an container that store the elements in dictionary as the key and their counts of occurence  in the dictionary values """

a = "aabbbcccc"
my_counter = Counter(a)
print(my_counter)
"""Counter({'c': 4, 'b': 3, 'a': 2})"""


"""if we use the items it will give use the key value pairs"""

print(my_counter.items())
"""dict_items([('a', 2), ('b', 3), ('c', 4)])
"""

"""we can get the keys and the values sepreately too"""

print(my_counter.keys())  # dict_keys(['a', 'b', 'c'])
print(my_counter.values())  # dict_keys(['a', 'b', 'c'])


"""find most common (argument )  argument will be like 1 or 2  or more 1 mean very first most common """

print(my_counter.most_common(1))  # [('c', 4)]
print(my_counter.most_common(2))  # [('c', 4), ('b', 3)]

"""to get the all elements of the iterable  """
print(my_counter.elements())  # <itertools.chain object at 0x000001CB813162F0>
print(list(my_counter.elements()))  # ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c']
