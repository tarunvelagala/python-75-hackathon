# inheritance program
class person:
    def __init__(self):
        self.name = input("name")
        self.age = int(input("age"))
        self.gender = input("gender")

    def display(self):
        print("name is:", self.name)
        print("age is:", self.age)
        print("gender is:", self.gender)


class marks:
    def __init__(self):
        self.stuclass = input("Class")
        print("enter marks of respective subject")
        self.literature = int(input("literature"))
        self.math = int(input("math"))
        self.biology = int(input("Biology"))
        self.physics = int(input("Physics"))

    def display(self):
        print("study in:", self.stuclass)
        print("total marks:", self.literature +
              self.math+self.biology+self.physics)


class student(person, marks):
    def __init__(self):
        person.__init__(self)
        marks.__init__(self)

    def result(self):
        person.display(self)
        marks.display(self)


stu1 = student()
stu2 = student()
stu1.result()
stu2.result()
