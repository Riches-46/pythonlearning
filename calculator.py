x  = 2
def addition(var1:int,var2:int):
    var3 = var1+var2
    print(x)
    return var3
def multiply(var1,var2):
    var3 = var1*var2
    print(var3)
    return var3


def main():
    a = float(input("enter number "))
    b = float(input("enter another number "))
    c = addition(a,b)
    print(f"value of c is {c}")
    d = multiply(a,c)
    print(f"value of d is {d}")
    print(x)
if __name__ == "__main__":
    main()
