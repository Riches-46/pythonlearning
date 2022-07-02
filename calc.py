def table_csv():

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

# This function divides two numbers
def divide(num1, num2):
    return num1 / num2

# shows user type of operation to be cacluated
print("Select operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

while True:
    # take input from the user
    select_operator = input("Enter operation to be calculated (1/2/3/4): ")

    # check if select_operator is one of the four options
    if select_operator in ('1', '2', '3', '4'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        #mathmatical calculations
        if select_operator == '1':
            print(num1, "+", num2, "=", add(num1, num2))
            results = add(num1, num2)
        elif select_operator == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
            results = subtract(num1, num2)
        elif select_operator == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
            results = multiply(num1, num2)
        elif select_operator == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            results = divide(num1, num2)
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break   
    else:
        print("Invalid Input")
def main():
    table_csv()
if __name__ == "__main__":
    main()
#populate table in csv     
file = open ("another_table.csv", "w")
file.write ("Number 1 Number 2 Result\n")
file.write ("{}       {}        {}      \n".format(num1, num2, results))
