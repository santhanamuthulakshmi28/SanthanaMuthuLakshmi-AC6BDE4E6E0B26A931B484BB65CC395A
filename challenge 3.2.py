#Implement a function called sort students that takes a list of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function with different input lists of students.and

class Student:

  def __init__ (self, name, roll_number, cgpa):
   self.name = name
   self.roll_number = roll_number
   self.cgpa = cgpa


def   sort_students (student_list): 

 sorted_students = sorted(student_list,key= lambda student: student.cgpa,reverse =True) 

 return sorted_students



students = [
        Student ("Vincy", "A123", 7.8),
        Student("Mala", "A124", 8.9),
        Student("Ananthi ", "A125", 9.1),
        Student("Nilofer", "A126", 9.9),
] 

sorted_students = sort_students(students) 


for student in sorted_students:
    print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
student.roll_number,
student.cgpa))