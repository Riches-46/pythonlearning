#Create a class
class newClass:
    x = 50 
    
print(newClass.x)

class newClass1:
    x = 100
#create a new object    
r = newClass1()
print(r.x)

class student:
    id = 10
    name = 'anderson'
    def display(self):
        print(self.id,self.name)

s = student()
s.display()

#init function
class student:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
s1 = student('harry', '24/06/1975')    
print(s1.name)
print(s1.dob)

#modify objects
s1.name = 'richard'
print(s1.name)

#delete objects
del s1.name
print(s1.name)
