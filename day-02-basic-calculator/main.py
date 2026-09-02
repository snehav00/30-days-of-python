print("=====================\n  PYTHON CALCULATOR\n=====================\n")


def calculate(a, operator, b):
    match operator:
        case "+":
            return a+b
        case "-":
            return a-b
        case "*": 
            return a*b
        case "/":
            return a/b
        case "%":
            return a%b
        case _:
            print("INVALID OPERATOR!\n")

try: 
    again = 'y'
    use = 'n'
    while again != 'x':
        
        if use != 'y':
            a = float(input("Enter first number: "))
        operator = input("Enter operator(+, -, *, /, %): ")
        b = float(input("Enter second number: "))
        result = calculate(a, operator, b)
        if result is None: 
            continue
        print(f"\nResult: {result}")
        
        again = (input("Enter 'x' to exit the calculator: ")).lower()
        if again!='x':
            use = (input(f"Do you want to use {result} further (y/n): ")).lower()
            if use == 'y':
                a = result
        
except ValueError:
    print("INVALID NUMBER")
except ZeroDivisionError:
    print("Can't divide by 0")

