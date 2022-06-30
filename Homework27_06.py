#define the function
def new():
    #create an empty list
    my_list1 = []
    # number of elements as input
    n = int(input("Enter amount of numbers in list : "))

    #asserts to make sure there are only 5 elements
    assert((n) == 5)  

    # iterating till the list is populated
    for i in range(0, n):
        num1 = int(input())
        # adding the element being input to the list
        my_list1.append(num1) 
    print(my_list1)
    
def main():
    new()
if __name__ == "__main__":
    main()
    
