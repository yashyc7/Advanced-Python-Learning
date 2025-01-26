"""
lists are ordered, mutable , allows duplicate methods 

.sort() method sorts the list but changes the original list

.sorted(<your_List>) sorts the list and returns the sorted list which you can store but dont modify the original list

.pop() method returns and remove the last element from the list 

.remove(<takes_element>) method is used to remove any specific element from the array

Slicing is a very nice way to access the subparts of your list with the colon(last index is excluded here)

if we dont specify the start index like mylist[:5] then it starts from the beggining and same for the end case if we dont specify the last index then it goes all the way till the end
[::1]
third argument is the optional index which is step which mean it reads and insert the every next item

we dont use assigning  for copying the lists
since they both refers to the same list in memory so in change in one list will also be reflecting in the other list as well which is not to be considered as the copied event

so for copying the lists in python we use the .copy method 

for eg. 
list_cpy=list(list_org) 

or 

list_cpy=list_org.copy()

or use the slicing 

list_cpy=list_org[:]  

from starting to the last index



list comprehension is the fast and elegant method to create the new list from the existing list here is the way to do that 


example_list=[1,2,3,4,5,6]

b=[i*i for i in example_list]

print(b)

so the output will be 

[1, 4, 9, 16, 25, 36]

"""


mylist=[2,4,6,8,-1,-2,-3]
print(mylist)



mylist2=[0]*5
print(mylist2)

new_list=mylist+mylist2

print(new_list) #concatenated list [2, 4, 6, 8, -1, -2, -3, 0, 0, 0, 0, 0]



#slicing concept

mylist3=[1,2,3,4,5,6,7,8,9]
a=mylist3[0:5]# 5th index will be excluded
print(a)
#so output will be depand on ,  since last index is excluded
#1,2,3,4,5

a=mylist3[::2]
print(f"{mylist3} after slicing and inserting the third optional argument of the step {a}")

#copying the list
list_org=["banana","cherry","apple"]

list_cpy=list_org #both list now refers to same list in memory

# strage thing happen here if i modify the copy then it also modify the original list too 
print("before assigning values")
print(list_org)
print(list_cpy)

list_cpy.append("lemon")
print("after assigning values")
print(list_cpy)
print(list_org) # it would also contains the lemon in it which is strange 


# so for copying the list in real case we have to do this


list_cpy=list_org.copy()
print("copied list",list_cpy)

list_cpy.append("Hello")
print(f"original list {list_org} is not modified when hello is entered in the copied list here is the copied list with the hello is appended {list_cpy}")



#list comprehension 

example_list=[1,2,3,4,5,6]

b=[i*i for i in example_list]

print(b)