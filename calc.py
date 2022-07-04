#main function
from pathlib import Path
import os
from re import A

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


def main():
    while True:
        # take input from the user
        select_operator = input("""Operation Types.\n
        (A) Addition\n(B) Subtraction\n(C) Multiplication\n(D) Division\n
        Enter operation to be calculated : """)
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: ")) 
        if select_operator.lower() == 'a':
            results = add(num1, num2)
            print(num1, "+", num2, "=", results)
            operator = "addition"
        elif select_operator.lower() == 'b':
            results = subtract(num1, num2)
            print(num1, "-", num2, '=', results)
            operator = "subtraction"
        elif select_operator.lower() == 'c':
            results = multiply(num1, num2)
            print(num1, "*", num2, '=', results)
            operator = "multiplication"
        elif select_operator.lower() == 'd':
            results = divide(num1, num2)
            print(num1, "/", num2, '=', results)
            operator = "division"
        else:
            print("Invalid Input")
        #populate table in csv     (Comma Seperated Values)
        file = open("C:\\Users\\ww\\another_table2.csv", "a")
        file.write("Number 1,Number 2,Operation,Result\n")
        file.write(f"{num1},{num2},{operator},{results}\n")
        
        
        next_calculation = input("would you like to do another calculation? (yes/no): ")
        if next_calculation.lower() == "no":
            break  
        
   

if __name__ == "__main__":
    main()
