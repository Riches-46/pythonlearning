class Father:
   num1 = 0
   def father(self):
    print(self.num1)

class Mother:
   num2 = 0
   def mother(self):
    print(self.num2)

class Grandparent(Father, Mother):
   def grandparent(self):
    print(self.num1)
    print(self.num2)

s1 = Grandparent()
s1.num1 = 2,10
s1.num2 = 5,-2
s1.grandparent()