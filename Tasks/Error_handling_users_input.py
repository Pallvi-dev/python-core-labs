try:
    num = int(input("Enter Number: "))
    result = 100/num
    print(result)

except ZeroDivisionError:
    print("can't divide by zero")

except ValueError:
    print("Enter valid number") 