print("=====================\n  PYTHON CALCULATOR\n=====================\n")
a = int(input("Enter first number: "))
operator = input("Enter operator(+, -, *, /): ")
b = int(input("Enter second number: "))

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

        
print(f"\nResult: {calculate(a, operator, b)}")
    