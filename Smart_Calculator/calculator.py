print("= SIMPLE CALCULATOR =")

first_value = float(input("Enter first number: "))
second_value = float(input("Enter second number: "))

user_choice = input("Choose operation (+, -, *, /): ")

if user_choice == "+":
    result = first_value + second_value

elif user_choice == "-":
    result = first_value - second_value

elif user_choice == "*":
    result = first_value * second_value

elif user_choice == "/":
    if second_value == 0:
        print("Division by zero is not allowed.")
        exit()
    result = first_value / second_value

else:
    print("Invalid operation selected.")
    exit()

print("Final Result:", result)
