def new():


    f = open("new_table.csv","w")
   

def additions(num1,num2):
    return num1+num2
    
def subtractions(num1,num2):
    return num1-num2
    
    #create an empty list
my_list1 = []
n = 1

# iterating till the list is populated
for i in range(0, n):
    operate = input("Enter A to operate or X to close")
    if operate == "A" or operate == "a":
        
        num1 = int(input("Enter the first number : "))
        num2 = int(input("Enter the second number : "))
        operator = input("Enter + for addition and - for subtraction : ")
        assert(num2 > 0)
    elif operator == "+":
        print(additions)
    elif operator == "-":
        print(subtractions)
        break  
print(my_list1)
    
def main():
    new()
if __name__ == "__main__":
    main()

#for i in range(0, n):
        #operate = input("Enter A to operate or X to close : ")
        #if operate == "A" or operate == "a":
            #num1 = int(input("Enter the first number : "))
            #num2 = int(input("Enter the second number : "))
            #operator = str(input("Enter either 1 for addition or 2 for subtraction : "))     
            #assert(num2 > 0) 
        #elif operate == "X" or operate == "x":
            #break          
file = open ("new_table.csv", "w")
file.write ("Number 1 Number 2 operation Result\n")
file.write ("{}       {}        {}      {} \n".format(num1, num2, operator,results))

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