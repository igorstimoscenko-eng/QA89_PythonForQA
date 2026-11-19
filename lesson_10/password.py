import re

def has_digit(password):
    return bool(re.search("\d",password))

print(has_digit("qwerty123"))
print(has_digit("qwerty"))