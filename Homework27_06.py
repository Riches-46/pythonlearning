#def myfunc():

my_list1 = []
 
    # number of elements as input
n = int(input("Enter number of elements : "))

    #asserts to make sure there are only 5 elements
assert((n) < 6 and (n) > 4)  

    # iterating till the list is populated
for i in range(0, n):
    ele = int(input())
    
    # adding the element being input to the list
    my_list1.append(ele) 
 
print(my_list1)