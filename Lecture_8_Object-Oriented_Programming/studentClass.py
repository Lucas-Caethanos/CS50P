class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


def get_student():
    name = input("Name: ")
    house = input("House: ")

    # Creating the object
    return Student(name, house)


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


if __name__ == '__main__':
    main()
