#Tuples :ordered , immutable , allows duplicate elements


mytuple=(3,4,"Max",True) #tuple

print(mytuple)

print(type(mytuple)) # class tuple


#single element would be considered as string
mytuple=("apple")

print(mytuple)

print(type(mytuple)) #class str


#to make it tuple

mytuple=tuple(["apple","banana","mango","cherry"])
print(mytuple)
print(type(mytuple))


## or use the , after the value to make it sure that it is tuple



mytuple2=("banana",)#adding comma after entry

print(mytuple2)

print(type(mytuple2))


#getting elements
item=mytuple[2]
print(item)

#It also supports the negative indexing


# mytuple[0]="Tim" throws error since tuple is immutable

# printing all the elements in it.
for x in mytuple:
    print(x)


#checking elements exist in it or not
if "cherry" in mytuple:
    print("yes") 
else:
    print("no")

#to get the length of the tuple

print(len(mytuple))

print(mytuple.count('cherry')) #return the number of occurences in tuple for example here the output is 1 since it exists only one time in the tuple 


print("first occurence of cherry in the tuple is at index ",mytuple.index("cherry"))#return the first occurence index of the element 


#converting the tuple to the list
 

mylist=list(mytuple)

print(mytuple)
print(mylist)


mytuple=tuple(mylist)
print(mytuple)
print(mylist)


#slicing with tuples

a=(2,3,4,23,53,25,64,52,51,54,32,52,1,0)

b=a[2:5] #output (4, 23, 53) since last index is excluded like 5th index 64 is excluded
print(b)

c=a[::2] # this 2 is the step 
print(c)


#to reverse the tuple


c=a[::-1]
print(c)


#Unpacking 

mytuple="Max",28,"Boston"

name,age,city=mytuple

print(name)
print(age)
print(city)

#no of variables on lhs == rhs otherwise the Value error may come like: too many values to unpack


#if some situations occur 

mytuple=(4,2,5,1,0,9,3,2)

i1,*i2,i3=mytuple
print(i1)
print(i2) #returns list after unpacking
print(i3)


#Comparing the tuple and list



