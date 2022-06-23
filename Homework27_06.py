
# creating an empty list
from re import A
from tkinter import N

#empty list
list1 = []
 
# number of elements as input
n = int(input("Enter number of elements : "))

#asserts to make sure there are only 5 elements
assert((n) < 6 and (n) > 4)  

# iterating till the list is populated
for i in range(0, n):
    ele = int(input())
    
    # adding the element being input to the list
    list1.append(ele) 
 
print(list1)