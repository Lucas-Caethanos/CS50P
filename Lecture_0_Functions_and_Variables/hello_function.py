

# Define a Main function
def main():
    name = input("What's your name? ")
    hello()
    hello(name)


# Create a new function (def for define) | Pass a default parameter (Word)
def hello(to="Word"):
    print("Hello,", to)


main()
