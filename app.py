from calc_func import do_sub, do_add
from multiply import do_multiply

def main():
    print("Wellcome to the calculator")
    print("""
        Select the function from the given options
          1. Add
          2. Subtract
          3. Multiply
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
    
    print('Result: ', result)

if __name__ == "__main__":
    main()