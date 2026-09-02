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
        case _:
            print("INVALID OPERATOR!")
            return

try: 
    again = 'y'
    use_answer = 'n'
    while again != 'x':
        
        a = int(input("Enter first number: "))
        operator = input("Enter operator(+, -, *, /): ")
        b = int(input("Enter second number: "))
        result = calculate(a, operator, b)
        print(f"\nResult: {result}")
        
        again = (input("Enter 'x' to exit the calculator and any key to continue: ")).lower()

except ValueError:
    print("INVALID NUMBER")

