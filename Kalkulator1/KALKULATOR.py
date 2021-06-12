#Python 3.9 Kalkulator

def calc(operator, x, y):
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "*":
        return x * y
    elif operator == "/":
        return x / y
    else:
        return None

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def calc(operator, x, y):
    if operator == "+":
        return add(x,y)
    if operator == "-":
        return add(x, y)
    if operator == "*":
        return add(x, y)
    if operator == "/":
        return divide(x, y)
    else:
        return None

def calc(operator, x, y):
    operators = {"+": add, "-": subtract, "*": multiply, "/": divide}
    method = operators.get(operator)
    if method:
        return method(x, y)

    return None

from operator import truediv, mul, add, sub

def calc(operator, x, y):
    operators = {"+": add, "-": subtract, "*": mul, "/": truediv}
    method = operators.get(operator, lambda x, y: None)
    return method (x, y)

def calculator():
    operation = None
    allowed_operations = ["+", "-", "*", "/"]
    while operation not in allowed_operations:
        operation = input(
            """
        Podaj operację jaką chcesz wykonać:
        + dodawanie
        - odejmowanie
        * mnożenie
        / dzielenie
            """
        )

    x = float(input("Podaj pierwszą liczbę: "))
    y = float(input("Podaj drugą liczbę: "))
    try:
        result = calc(operation, x, y)
    except ZeroDivisionError:
        print("Nie można dzielić przez zero")
    else:
        print(result)

    #KALKULATOR

operation = input(
            """
        Podaj operację jaką chcesz wykonać:
        + dodawanie
        - odejmowanie
        * mnożenie
        / dzielenie
            """
        )

x = float(input("Podaj pierwszą liczbę: "))
y = float(input("Podaj drugą liczbę: "))
try:
    result = calc(operation, x, y)
except ZeroDivisionError:
    print("Nie można dzielić przez zero")
else:
    print(result)