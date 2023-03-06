import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []

print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

for n in range(0, nr_letters):
    password.append(random.choice(letters))

for n in range(0, nr_symbols):
    password.append(random.choice(symbols))

for n in range(0, nr_numbers):
    password.append(random.choice(numbers))

holder = ""
add_order_pass = ""
random_order_pass = ""

# Saving the password in the append order
for char in password:
    add_order_pass += char

# Changing the order of the characters in the password
# random.shuffle could be used, but here I chose to use the logic approach
for n in range(0, len(password)):
    random_position = random.randint(0, len(password)-1)  # Generates a random position between 0 and the password size
    for char in password:
        # Swap the position of each character to a random one using a holder variable
        holder = password[n]  # First save the character that is in the n position
        password[n] = password[random_position]  # Then change the n position character to the random position
        password[random_position] = holder  # Now change the character in the random position to the one saved

# Saving the randomized order password
for char in password:
    random_order_pass += char
print(f"Password in append order: {add_order_pass}")
print(f"Password in random order: {random_order_pass}")
input("Press enter to exit.")