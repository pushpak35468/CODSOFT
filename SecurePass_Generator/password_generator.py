import random
import string


password_length = int(input("Enter password length: "))

all_characters = string.ascii_letters + string.digits + string.punctuation

generated_password = ""

for i in range(password_length):
    generated_password += random.choice(all_characters)

print("\nYour Password Is:")
print(generated_password)
if password_length < 6:
    print("Password Strength: Weak")
elif password_length < 10:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")







