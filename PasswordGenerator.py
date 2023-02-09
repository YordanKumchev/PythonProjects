print("""The idea behind this simple program is to generate a user passowrd
      that is based on his/hers preferences""")

import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
numbers = "1234567890"
symbols = "!@#$%^&*()_+{};;\|<>?"


length = int(input("How long do you want your password to be (1-50 symbols)?: "))
    
print("""You are presented with 6 methods to choose from:
    (1)Lowercase and uppercase letters, numbers and symbols?
    (2)Lowercase letters, numbers and symbols only?
    (3)Uppercase letters, numbers and symbols only?
    (4)Lowercase letters and symbols only?
    (5)Uppercase letters and symbols only?
    (6)Numbers and symbols only?""")

pwtype = int(input("Select a method from 1 through 6: "))

# Password types
type1 = lower + upper + numbers + symbols
type2 = lower + numbers + symbols
type3 = upper + numbers + symbols
type4 = lower + symbols
type5 = upper + symbols
type6 = numbers + symbols

if pwtype == 1:
    password = "".join(random.sample(type1, length))
    print(f"Our recommended password is: {password}")
elif pwtype == 2:
    password = "".join(random.sample(type2, length))
    print(f"Our recommended password is: {password}")
elif pwtype == 3:
    password = "".join(random.sample(type3, length))
    print(f"Our recommended password is: {password}")
elif pwtype == 4:
    password = "".join(random.sample(type4, length))
    print(f"Our recommended password is: {password}")
elif pwtype == 5:
    password = "".join(random.sample(type5, length))
    print(f"Our recommended password is: {password}")
elif pwtype == 6:
    password = "".join(random.sample(type6, length))
    print(f"Our recommended password is: {password}")
else:
    print("You haven't selected a valid password combination")