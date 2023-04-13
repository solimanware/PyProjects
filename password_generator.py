import random
import string

number_of_letters = int(input("What's the number of letters in the password? "))
number_of_digits = int(input("What's the number of digits in the password? "))
number_of_special_characters = int(input("What's the number of special characters in the password? "))

letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
digits = list(string.digits)
special_characters = list(''' !”#$%&’()*+,-./:;<=>?@[\\]^_`{|}~''')

password_list = []
for _ in range(number_of_letters):
    password_list.append(random.choice(letters))
for _ in range(number_of_digits):
    password_list.append(random.choice(digits))
for _ in range(number_of_special_characters):
    password_list.append(random.choice(special_characters))

random.shuffle(password_list)
print(''.join(password_list))
