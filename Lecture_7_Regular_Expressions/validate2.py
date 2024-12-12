import re

email = input("What's your email? ").strip()

# [^@] -> any character except an @ sign
# Raw string
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):

# \w -> "word character"
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
