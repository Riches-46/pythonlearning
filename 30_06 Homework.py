import csv

def additions(var1:int,var2:int):
    var3 = var1+var2
    return var3


with open('myTable.csv','w+') as f:
    table = csv.writer(f)
    #write a csv header
    table.writerow(["num1","num2","operation","results"])
    #gets input from user
    numb1 = input("Please enter first number :")
    numb2 = input("Please enter second number :")
    operation1 = input("Please enter a math function :")
    

    table.writerow([numb1,numb2,operation1,results])