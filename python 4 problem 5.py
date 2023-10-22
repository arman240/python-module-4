correct_username = "python"
correct_password = "rules"
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        print("Access denied")
        attempts += 1
if attempts == max_attempts:
    print("Maximum login attempts reached. Access denied.")
