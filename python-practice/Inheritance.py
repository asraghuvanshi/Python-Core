class Student:
    def __init__(self ,name , uid, age):
        self.name = name
        self.uid = uid
        self.age = age
    def getDetails(self):
        print(f"Name is : {self.name}\nUID is: {self.uid} \nAge is: {self.age}")


class Employee(Student):
    def __init__(self, name, uid, age):
        self.name = name
        self.uid = uid
        self.age = age

    def getData(self):
        print(self.name , self.uid, self.age)

obj = Employee("Amit","20MCA144",22)
obj.getDetails()
