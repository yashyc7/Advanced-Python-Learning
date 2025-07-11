class Person:
    name="harry"
    occupation="software developer"
    net_worth=100000
    
    def info(self):
        print(f"{self.name} is a {self.occupation}")


a=Person()
a.name="yash"
print(a.name)

print(a.info())
