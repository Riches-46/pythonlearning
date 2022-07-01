import csv

#num1 = []
#num2 = []
#operation = []
#finalResults = []

with open('myTable.csv','w+') as f:
    table = csv.writer(f)
    #write a csv header
    table.writerow(["num1","num2","operation","results"])
    #gets input from user
    numb1 = input("Please enter first number :")
    numb2 = input("Please enter second number :")
    operation1 = input("Please enter a math function :")
    
    table.writerow([numb1,numb2,operation1])