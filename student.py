class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        person_info = super().display_info()
        return f"{person_info}, Student ID: {self.student_id}"


if __name__ == "__main__":
    print("\nPersons\n")
    person1 = Person("Estong", 24)
    person2 = Person("Buloy", 26)
    person3 = Person("Obet", 25)
    person4 = Person("Loloy", 49)
    person5 = Person("Gahi", 42)
    print(person1.display_info())
    print(person2.display_info())
    print(person3.display_info())
    print(person4.display_info())
    print(person5.display_info())

    print("\nStudents\n")
    student1 = Student("Ryan Kenneth Regato", 27, "20235017")
    student2 = Student("Jhon Louie Pangandoyon", 20, "20235070")
    student3 = Student("Dwiaght Sisles", 22, "20235092")
    student4 = Student("Jenelyn Oling", 22, "20213055")
    student5 = Student("Retchie Talisic", 24, "20235003")
    print(student1.display_info())
    print(student2.display_info())
    print(student3.display_info())
    print(student4.display_info())
    print(student5.display_info())