class Student:
    def __init__(self, name, house):

        # Instance variable names cannot be the same as functions
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter
    @property
    def house(self):
        return self._house

    # Setter - will get called any time that the user access .house
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name


def get_student():
    name = input("Name: ")
    house = input("House: ")

    # Creating the object
    return Student(name, house)


def main():
    student = get_student()

    # The attribute must not be accessed directly
    # student._house = "Number four, Privet Drive"
    print(student)


if __name__ == '__main__':
    main()
