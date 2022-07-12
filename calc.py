from pathlib import Path
import logging
import datetime
# addition function
def add(num1, num2):
    logger1.info("add function")
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
    
def initializing_log():
    #logging 
    dir_data = Path("test_logs")
    dir_data.mkdir(parents=True, exist_ok=True)
    log_filename = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
    print(log_filename)

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d-%Y %H:%M:%S',
                        filename=f'test_logs/{log_filename}.log',
                        filemode='w')
    global logger1
    logger1 = logging.getLogger("example")
#logging.basicConfig(filename='new_log.log',
                    #format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    #datefmt='%m-%d-%Y %H:%M:%S',
                    #level=logging.DEBUG)

def main():
    initializing_log()
    dir_data = Path("output")
    dir_data.mkdir(parents=True, exist_ok=True)
    
    
    filepath = dir_data / "file.csv"
    if not filepath.is_file():
        with open(filepath, "a") as f:
            f.write(f"Number 1,Number 2,Operation,Result\n")

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
            logging.debug('check for addition')
        elif select_operator.lower() == 'b':
            results = subtract(num1, num2)
            print(num1, "-", num2, '=', results)
            operator = "subtraction"
            logging.debug('check for subtraction')
        elif select_operator.lower() == 'c':
            results = multiply(num1, num2)
            print(num1, "*", num2, '=', results)
            operator = "multiplication"
            logging.debug('check for multiplication')
        elif select_operator.lower() == 'd':
            results = divide(num1, num2)
            print(num1, "/", num2, '=', results)
            operator = "division"
            logging.debug('check for division')
        else:
            print("Invalid Input")
          
        with open(filepath, "a") as f:
            f.write(f"{num1},{num2},{operator},{results}\n")
        
        next_calculation = input("would you like to do another calculation? (yes/no): ")
        if next_calculation.lower() == "no":
          break    
        print(main('select_operator'))           
   

if __name__ == "__main__":
    main()
