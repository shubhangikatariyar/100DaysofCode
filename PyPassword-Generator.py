import random

print("Welcome to the PyPassword Generator!")

letter=int(input("How many letters would you like in your password?\n"))

symbol=int(input("How many symbols would you like in your password?\n"))

number=int(input("How many numbers would you like in your password?\n"))

# A 65 +26 = 91
# a 97 +26 = 123

# Type | Code | Example Output
# Lowercase Letters | list(string.ascii_lowercase) | ['a', 'b', ..., 'z']
# Uppercase Letters | list(string.ascii_uppercase) | ['A', 'B', ..., 'Z']
# Digits | list(string.digits) | ['0', '1', ..., '9']
# Symbols | list(string.punctuation) | ['!', '@', '#', ..., '~']

# Lowercase letters
lowercase_letters = [chr(i) for i in range(97, 123)]  # 'a' to 'z'

# Uppercase letters
uppercase_letters = [chr(i) for i in range(65, 91)]   # 'A' to 'Z'

# All letters
all_letters = lowercase_letters + uppercase_letters

# Digits
digits = [chr(i) for i in range(48, 58)]  # '0' to '9'

# Symbols
symbols = [chr(i) for i in range(33, 48)] + [chr(i) for i in range(58, 65)] + \
          [chr(i) for i in range(91, 97)] + [chr(i) for i in range(123, 127)]


# EASY LEVEL
password=''
while letter!=0:
    password+=random.choice(all_letters)
    letter-=1
while symbol!=0:
    password+=random.choice(symbols)
    symbol-=1
while number!=0:
    password+=random.choice(digits)
    number-=1


# HARD LEVEL
lst_pass= list(password)
random.shuffle(lst_pass)  # RANDOM SHUFFLE WORKS ONLY ON LIST 
password ="".join(lst_pass)  # JOINING LIST TO STRING
print(f"Your password is: {password}")



# # OUTPUT:
# Welcome to the PyPassword Generator!
# How many letters would you like in your password?
# 6
# How many symbols would you like in your password?
# 3
# How many numbers would you like in your password?
# 3
# Your password is: |2/zgl0IE7=T