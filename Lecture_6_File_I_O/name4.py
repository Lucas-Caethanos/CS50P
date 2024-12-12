
names = []

# By default, the open function reads the file ("r")
with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())
        # names.append(line.rstrip())

# for name in sorted(names):
#     print(f"hello, {name}")
