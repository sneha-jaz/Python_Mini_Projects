#Password Generator
import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

print("**** Welcome to the Python Password Generator! ****")
no_letters = int(input("How many letters would you like in your password?\n"))
no_symbols = int(input(f"How many symbols would you like in your password?\n"))
no_numbers = int(input(f"How many numbers would you like in your password?\n"))

#Eazy password - example JgpAl+@)6920
# password = ""
# for char in range(1, no_letters + 1):
#   password += random.choice(letters)

# for char in range(1, no_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, no_numbers + 1):
#   password += random.choice(numbers)

# print(f"Your easy password is: {password}")

#Hard password - example J+0lg96pA@2)
password_list = []

for char in range(1, no_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, no_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, no_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"\nYour password is: {password}")
