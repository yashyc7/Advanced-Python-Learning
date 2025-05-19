a = input("enter any value between 5 and 9 ")

if type(a) == int:
    if a < 5 or a > 9:
        raise ValueError("value should be between 5 and 9")
else:
    raise TypeError("value should be the integer")
