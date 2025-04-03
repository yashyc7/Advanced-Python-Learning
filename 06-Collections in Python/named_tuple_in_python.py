from collections import namedtuple

"""easy to crate and lightweight object type
similiar to struct """


"""Point =namedtuple(<class_name>,'x,y')"""

Point = namedtuple("Point", "x,y")


pt = Point(1, -4)

print(pt)  # Point(x=1, y=-4)
