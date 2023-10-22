smallest = None
largest = None
while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break
    try:
        number = float(user_input)
        if smallest is None or number < smallest:
            smallest = number
        if largest is None or number > largest:
            largest = number
    except ValueError:
        print("Invalid input. Please enter a number.")
if smallest is not None and largest is not None:
    print(f"The smallest number is: {smallest}")
    print(f"The largest number is: {largest}")
else:
    print("No valid numbers were entered.")
