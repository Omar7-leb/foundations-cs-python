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