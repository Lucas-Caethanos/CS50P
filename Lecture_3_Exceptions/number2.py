
def get_int():
    while True:
        try:
            x = int(input("What's x? "))

        except ValueError:
            # print("x is not an integer")
            pass

        else:
            # break
            return x


def main():
    x = get_int()
    print(f"x is {x}")


main()
