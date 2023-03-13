try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    division = first_number / second_number
    print(division)
except ValueError:
    print("Incorrect value")
except ZeroDivisionError:
    print("Division by 0 is not possible")
