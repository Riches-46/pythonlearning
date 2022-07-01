import csv

#num1 = []
#num2 = []
#operation = []
#finalResults = []

with open('myTable.csv','w+') as f:
    table = csv.writer(f)
    table.writerow(["num1","num2","operation","results"])
    num1 = input("Please enter first number :")
    num2 = input("Please enter second number :")
    operation = input("Please enter a math function :")
    table.writerow([num1,num2,operation])