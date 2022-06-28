
def addition(var1:int,var2:int):
    var3 = var1+var2
    #print(x)
    return var3
def multiply(var1:int,var2:int):
    var3 = var1*var2
    #print(var3)
    return var3
def subtraction(var1:int,var2:int):
    var3 = var1-var2
    #print(x)
    return var3
def division(var1:int,var2:int):
    var3 = var1/var2
    #print(var3)
    return var3

def new():
    #create an empty list
    my_list1 = []
    n = 1
    # iterating till the list is populated
    for i in range(0, n):
        operate = input("Enter A to operate or X to close")
        if operate == "A" or operate == "a":
            num1 = int(input("Enter the first number"))
            num2 = int(input("Enter the second number"))
            assert(num2 > 0)
            # adding the element being input to the list
            my_list1.append(division(num1,num2))
        elif operate == "X" or operate == "x":
            break
    for i in range(0, n):
        operate = input("Enter A to operate or X to close")
        if operate == "A" or operate == "a":
            num1 = int(input("Enter the first number"))
            num2 = int(input("Enter the second number"))
            assert(num2 > 0)
            # adding the element being input to the list
            my_list1.append(addition(num1,num2))
        elif operate == "X" or operate == "x":
            break    
    print(my_list1)
    
def main():
    new()
if __name__ == "__main__":
    main()


#limitations 
#1. issue with storing in list 
#2. what if user performs more then 1000 operations
#3. we dont know the type of operation in the background