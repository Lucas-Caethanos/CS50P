class Student:
    def __init__(self, name, house, patronus):

        if not name:
            raise ValueError("Missing name")

        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")

        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "Stag"
            case "Otter":
                return "Otter"
            case "Jack Russell Terrier":
                return "Jack Russell Terrier"
            case _:
                return "Not Patronus"


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")

    # Creating the object
    return Student(name, house, patronus)


def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())


if __name__ == '__main__':
    main()
