#FSW
#1----------------------------------------------------------------
def GetStudentById(student_data, ID):
    for student in student_data:
        if student['ID'] == ID:
            return student
        
#2----------------------------------------------------------------
def GetAllStudents(student_data):
    return student_data

#3----------------------------------------------------------------
def GetStudentByMajor(student_data, major):
    commonMajor = []
    for student in student_data:
        if student["Major"] == major:
            commonMajor.append(student["Name"])
    return commonMajor

#4----------------------------------------------------------------
def addStudent(student_data, id, name, age, major, GPA):
    new_student = {"ID": id, "Name": name, "Age": age, "Major": major, "GPA": GPA}
    student_data.append(new_student)
    print("Student added successfully")

#5----------------------------------------------------------------
def CommonMajor(student_data, student_data_2):
    common_Students = set()
    for student in student_data:
        for student2 in student_data_2:
            if student['Major'] == student2["Major"]:
                common_Students.add(student["Major"])
    return common_Students

#6-----------------------------------------------------------------
def delete_student(students, id):
    updated_students = [student for student in students if student['ID'] != id]
    if len(updated_students) == len(students):
        print("Student not found!")
    else:
        print("Student with ID:", id, "was deleted successfully.")
    return updated_students


