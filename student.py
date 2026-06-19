class Student:

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)

    def result(self):
        if self.marks >= 35:
            print("Result: Pass")
        else:
            print("Result: Fail")


students = []

while True:

    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        marks = int(input("Enter Marks: "))

        s = Student(name, age, marks)
        students.append(s)

        print("Student Added!")

    elif choice == "2":

        for student in students:
            student.show()
            student.result()
            print("-" * 20)

    elif choice == "3":

        search_name = input("Enter Name to Search: ")

        for student in students:
            if student.name == search_name:
                student.show()
                student.result()

    elif choice == "4":

        delete_name = input("Enter Name to Delete: ")

        for student in students:
            if student.name == delete_name:
                students.remove(student)
                print("Student Deleted!")
                break

    elif choice == "5":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
