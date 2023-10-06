class student:
  def__init__(self,name,roll_number,cgpa)
  Self.name=Name
  Self.roll_number=roll_number
  Self.cgpa=cgpa
  def sort_student(student_list):
  #sort student in the descending order of CGPA
  sorted_student=sorted(student_list,key=lambda student: student.cgpa,reverse=true)
return sorted_student
student=[
  student("Anu","A123","8.6"),
  student("Jimim","A124","9.2"),
  student("Kakashi","A125","9.6"),
  student("Sasuke","A126","9.8")
]
sorted_student=sort_student(student)
for student in sorted_student
print("name:{}","roll_number:{}", "CGPA:{}".format (student.name,student.roll_number,student.cgpa))