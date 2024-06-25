def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def calculator():
    print("Simple Calculator")
    
    # Get input from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice == '1':
        print(f"The result of {num1} + {num2} is {add(num1, num2)}")
    elif choice == '2':
        print(f"The result of {num1} - {num2} is {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result of {num1} * {num2} is {multiply(num1, num2)}")
    elif choice == '4':
        result = divide(num1, num2)
        if result == "Error! Division by zero.":
            print(result)
        else:
            print(f"The result of {num1} / {num2} is {result}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    calculator()
