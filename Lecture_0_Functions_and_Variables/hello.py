
# Ask user for their name
name = input("What's is your name? ")
# name = input("What's is your name? ").strip().title()

# Remove whitespace from str
# name = name.strip()

# Capitalize user's name (only the first name)
# name = name.capitalize()

# Capitalizing the first letter of each word
# name = name.title()

# Chain these functions together
name = name.strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

# Say hello to user
print("Hello,", first)
print("Hello,", last)
print(f"Hello, {name}")

# Scape character
print("Hello, \"friend\"")
print("Hello, 'friend'")





