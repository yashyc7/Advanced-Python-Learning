from collections import OrderedDict

"""Its like normal dictionay but it remembers the orders of the items in which they were placed in."""

ordered_dict = OrderedDict()

ordered_dict["a"] = 1
ordered_dict["b"] = 2
ordered_dict["c"] = 3
ordered_dict["d"] = 4
ordered_dict["e"] = 5

print(ordered_dict)  # OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
