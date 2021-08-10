"""
You need to write regex that will validate a password to 
make sure it meets the following criteria:

At least six characters long
contains a lowercase letter
contains an uppercase letter
contains a number
Valid passwords will only be alphanumeric characters.
"""
from re import search

regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{6,}$"


print(bool(search(regex, "jfkdfj3j")))  # False
print(bool(search(regex, "djI38D55")))  # True
