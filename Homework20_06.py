#defining a function that subtracts
def subtract(var1:int,var2:int):
    var3 = var1 + var2
    return (var3)
#defining a function that divides
def division(var1,var2):
    var3 = var1 + var2
    return (var3)

#main
def main():
    a = (input("enter number "))
    b = (input("enter another number "))
    c = subtract(a,b)
    print(f"value of c is {c}")
    d = division(a,b)
    print(f"value of d is {d}")
if __name__ == "__main__":
    main()