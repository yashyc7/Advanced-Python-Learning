# Dictionary : Key value pairs, Unordered, Mutable

mydict = {"name": "Max", "age": 28, "city": "New York"}

print(mydict)

mydict2 = dict(name="Mary", age=27, city="Washington DC")

print(mydict2)

value = mydict2["name"]
print(value)


mydict["email"] = "max@gmail.com"

print(mydict)

# to delete the key value pair

del mydict["name"]


# or we can use the pop method

mydict.pop("age")

# remove the last item from the dictionary by pop item method

print(mydict2.popitem())


if "name" in mydict2:
    print(mydict2["name"])
else:
    print("nothing is present like key name")


try:
    print(mydict["name"])
except:
    print("Error")


for key in mydict2.keys():  # .keys method returns the list of all the keys inside it.
    print(key)  # ["name","age"]


# for looping through the values

for value in mydict2.values():
    print(value)  # ["Mary",27]

print(mydict)
print(mydict2)

mydict_cpy = mydict

mydict_cpy["name"] = (
    "Max"  # adding values in assigned dict add values also in original dict "mydict"
)

print(mydict_cpy)
print(mydict)

# so it was not the way to copy the dictionary
# the correct way is
mydict_cpy = mydict.copy()

mydict_cpy["college"] = "MIT"

print(mydict_cpy)
print(mydict)


# updating the dictionaries
mydict = {"name": "Max", "age": 28, "email": "example@xyz.com"}
mydict2 = dict(name="Mary", age=27, city="Boston")

print(mydict)
print(mydict2)

mydict.update(mydict2)
print(mydict)
# updates the key overwrite the value of the occuring key


# Miscellenous cases

mydict = {3: 9, 6: 43, 9: 81}
print(mydict)
value = mydict[9]
print(value)

mytuple = (
    8,
    7,
)  # we can use the tuple here but cant use the list here since List is mutable
mydict = {mytuple: 15}
print(mydict)
