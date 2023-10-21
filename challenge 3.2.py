#3.2 Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object has the following attributes: name (string)       roll number (string), and cgpa (float). Test the function with different input lists of studentsc
class Student:
    def __init__(self, name, roll_number, cgpa):

        self.name = name
      
        self.roll_number= roll_number

        self.cgpa = cgpa



def sort_students (student_list):

    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)

    return sorted_students
student1 = Student("Alice", "S123", 3.7)

student2 = Student("Bob","S124", 3.9)

student3 = Student("Charlie",  "S125", 3.5)

student4 = Student("David", "S126", 3.8)
      


students = [student1, student2, student3, student4]



sorted_students =       sort_students (students)


for student in sorted_students:

    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")