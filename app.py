from calc_func import do_sub, do_add, do_div
from multiply import do_multiply
from area import calculate_area

def main():
    print("Wellcome to the calculator")
    print("""
        Select the function from the given options
          1. Add
          2. Subtract
          3. Multiply
          4. Div
""")
    
    user_input = input("Select the function : ")

    a = int(input("Valu of A : "))
    b = int(input("Valu of B : "))

    if user_input == "1":
        result = do_add(a,b)
    elif user_input == "2":
        result = do_sub(a,b)
    elif user_input == "3":
        result = do_multiply(a,b)
    elif user_input == "4":
        result = do_div(a,b)
    
    print('Result: ', result)

if __name__ == "__main__":
    main()