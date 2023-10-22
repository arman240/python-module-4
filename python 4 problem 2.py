while True:
    inches = float(input("Enter a value in inches (or a negative value to quit): "))
    if inches < 0:
        break
    centimeters = inches * 2.54
    print(f"{inches} inches is equal to {centimeters} centimeters.")
