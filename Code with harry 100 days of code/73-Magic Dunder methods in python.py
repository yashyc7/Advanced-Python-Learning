class Employee:
    name="Harry"
    
    def __len__(self):
        sum=0
        for character in self.name:
            sum+=1
        return sum


e=Employee()
print(e.name)
print(len(e.name))
print(len(e)) #using the dunder method where we are sending only object 

#now using the __str__ and __repr__ methods




class Employee2:
    name="Harry"
    
    def __init__(self,name):
        self.name=name
        
    def __str__(self):
        return (f"The name of the employee is {self.name} by str")
    
    def __repr__(self):
        return (f"The name of the employee is {self.name} by repr")
    
    # str vs repr:we can recereate object by the repr method 
    def __call__(self):
        print("Hey i am good ")
e=Employee2("yash")
print(e.name)
print(e)
e()

#now call method

