def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    if b==0:
        return "Error: Division by zero: Invalid"
    return a/b

def percentage(a,b):
    if b==0:
        return "Error: Invalid Inputs"
    return (a/b)*100

while True:
    print("\n=== CLI Calculator ===")
    print("+ Addition")
    print("- Subtraction")
    print("* Multiplication")
    print("/ Division")
    print("% Percentage")
    print("exit Quit")

    choice = input("Enter choice: ").lower()

    if choice == "exit":
        print("Goodbye...")
        break

    if choice not in ["+", "-", "*", "/", "%"]:
        print("Invalid choice. Try again.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Enter valid numbers.")
        continue

    if choice == "+":
        print("Result:", add(num1, num2))
    elif choice =="-":
        print("Result:", subtract(num1, num2))
    elif choice =="*":
        print("Result:", multiply(num1, num2))
    elif choice =="/":
        print("Result:", divide(num1, num2))
    elif choice =="%":
        print("Result:", percentage(num1, num2))