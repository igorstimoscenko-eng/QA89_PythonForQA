#Low level - > It only performs calculation and doesn't interact with user
def calculate(a:float, b:float,op:str):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        return a/b #Zero devisionError if b==0

#Middle level -> parsing Convert string into numbers
def pars(a_str:str,b_str:str,op:str):
    a = float(a_str) #If not a number ->ValueError
    b = float(b_str) #If not a number ->ValueError
    return calculate(a,b,op)