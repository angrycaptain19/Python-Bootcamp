#Calcy

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations ={
    "+":add,
    "-":sub,
    "*":multiply,
    "/":divide
}

def calcy():
    num1 = float(input("Enter First Number: "))
    for symbols in operations:
        print(symbols)
    should_continue = True
    while should_continue:
        operations_symbols = input("Pick the operation from above line:  ")
        num2 = float(input("Enter Next Number: "))
        calculation_function = operations[operations_symbols]
        answer = calculation_function(num1,num2)
        print(f"{num1} {operations_symbols} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calcy()

calcy()