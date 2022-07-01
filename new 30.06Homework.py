def additions(num1:int,num2:int):
    num3 = num1+num2
    return num3
def subtractions(num1:int,num2:int):
    num4 = num1-num2
    return num4

n = 1


f = open("new_table.csv","w")
   
#num1 = input ("Enter first number: ")
#num2 = input("Enter Second number: ")
#operator = input("Please enter either addition or subtraction: ")

for i in range(0, n):
        operate = input("Enter A to operate or X to close : ")
        if operate == "A" or operate == "a":
            num1 = int(input("Enter the first number : "))
            num2 = int(input("Enter the second number : "))
            operator = str(input("Enter either 1 for addition or 2 for subtraction : "))     
            assert(num2 > 0) 
        elif operate == "X" or operate == "x":
            break          
file = open ("new_table.csv", "w")
file.write ("Number 1 Number 2 operation Result\n")
file.write ("{}  {}  {}   {} \n".format(num1, num2, operator, results))

#def new():
    #create an empty list
    #my_list1 = []
    #n = 1
    # iterating till the list is populated
    #for i in range(0, n):
        #operate = input("Enter A to operate or X to close")
        #if operate == "A" or operate == "a":
            #num1 = int(input("Enter the first number"))
            #num2 = int(input("Enter the second number"))
            #assert(num2 > 0)
            # adding the element being input to the list
            #my_list1.append(addition(num1,num2))
        #elif operate == "X" or operate == "x":
            #break   
    #print(my_list1)
    
#def main():
    #new()
#if __name__ == "__main__":
    #main()







file.close()