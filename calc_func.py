#Addition
def do_add(a:int, b:int):
    return a+b

#Subtraction
def do_sub(a:int, b:int):
    return a-b

def do_div(a:int, b:int):
    try:
        return a/b
    except ZeroDivisionError as e:
        return "Cannot divide by zero"