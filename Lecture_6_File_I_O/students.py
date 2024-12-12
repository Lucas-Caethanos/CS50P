def get_name(student):
    return student["name"]


students = []

with open("students.csv") as file:
    for line in file:
        # row = line.rstrip().split(",")
        # print(f"{row[0]} is in {row[1]}")

        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

# The sorted function uses the "name" key to sort the values. Sorted calls the get_name function for each student
# for student in sorted(students, key=get_name):

# Equivalent to the get_name function.
# The lambda keyword represents an anonymous function that returns the key "name" to be sorted
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} in in {student['house']}")
