#main function
def table_csv():
    #creates and writes to a csv file
    f = open("another_table.csv", "w")

# addition function
def add(num1, num2):
    return num1 + num2

# subtraction function
def subtract(num1, num2):
    return num1 - num2

# multiplication function
def multiply(num1, num2):
    return num1 * num2

# Division function 
def divide(num1, num2):
    return num1 / num2

# shows user type of operation to be cacluated
print("Operation Types.")
print("Addition")
print("Subtraction")
print("Multiplication")
print("Division")

while True:
    # take input from the user
    select_operator = input("Enter operation to be calculated : ")

    # check if select_operator is one of the four options
    if select_operator in ('Addition', 'Subtraction', 'Multiplication', 'Division'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        #mathmatical calculations
        if select_operator == 'Addition':
            print(num1, "+", num2, "=", add(num1, num2))
            results = add(num1, num2)
            operator = "addition"
        elif select_operator == 'Subtraction':
            print(num1, "-", num2, "=", subtract(num1, num2))
            results = subtract(num1, num2)
            operator = "subtraction"
        elif select_operator == 'Multiplication':
            print(num1, "*", num2, "=", multiply(num1, num2))
            results = multiply(num1, num2)
            operator = "multiplication"
        elif select_operator == 'Division':
            print(num1, "/", num2, "=", divide(num1, num2))
            results = divide(num1, num2)
            operator = "division"
        # check if user wants another calculation
        # break the loop if answer is no
        next_calculation = input("would you like to do another calculation? (yes/no): ")
        if next_calculation == "no":
          break   
    else:
        print("Invalid Input")

def main():
    table_csv()
if __name__ == "__main__":
    main()
#populate table in csv     
file = open("another_table.csv", "w")
file.write ("Number 1 Number 2 Operation Result\n")
file.write ("{:>15} {:>15} {:>10} {:>10} \n".format(num1, num2, operator, results))
