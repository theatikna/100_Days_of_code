import random
import string 
letters = string.ascii_letters
numbers = string.digits
symbol = string.punctuation
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
password = [random.choice(letters) for x in range(nr_letters)] + [random.choice(numbers) for x in range(nr_numbers)] + [random.choice(symbol) for x in range(nr_symbols)]
random.shuffle(password)
password_s = ''.join(password)
print(f"Your Password is : {password_s}")
