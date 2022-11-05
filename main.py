import random

letters = 'abcdefghijklmnoprstuvwxyz'
numbers = [i for i in range(10)]
simbols = "!#$%&'()*+,-."
password_list = []
# Define your custom size:
pass_size = 12
max_simbols = 2
max_numbers = 2
max_letters = pass_size - (max_simbols + max_numbers)

for i in range(max_simbols):
    password_list.append(random.choice(simbols))
for i in range(max_numbers):
    password_list.append(random.choice(numbers))
for i in range(max_letters):
    password_list.append(random.choice(letters))

random.shuffle(password_list)
password = ''
for element in password_list:
    password += str(element)

print(password)