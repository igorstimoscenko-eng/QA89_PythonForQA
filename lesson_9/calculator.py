#Low level - > It only performs calculation and doesn't interact with user
def calculate(a:float, b:float,op:str):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        return a/b #ZeroDevisionError if b==0

#Middle level -> parsing Convert string into numbers
def pars(a_str:str,b_str:str,op:str):
    a = float(a_str) #If not a number ->ValueError
    b = float(b_str) #If not a number ->ValueError
    return calculate(a,b,op)

#Top level -> dialog  It captures everything and explains it to the user
def run_calculator():
    try:
        a = input("Enter the first number: ")
        b = input("Enter the second number: ")
        op = input("Enter Actions (+,-,*,/): ")
        result  = pars(a,b,op)
        print(f"Result:{result}")
    except ValueError as e:
        print(f"Invalid data: {e}")
    except ZeroDivisionError:
        print(f"You can't divide by zero")

run_calculator()