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

#7----------------------------------------------------------------
def Average(student_data):
    totalGPA = 0
    count = 0
    for student in student_data:
        if "GPA" in student:
            totalGPA += student["GPA"]
            count += 1
    if count == 0:
        return 0
    return totalGPA / count

#8----------------------------------------------------------------
def TopPerformances(student_data, limit):
    student_gpa = []
    top_student_names = []

    for student in student_data:
        if "GPA" in student:
            student_gpa.append(student["GPA"])

    student_gpa_sorted = sorted(student_gpa, reverse=True)

    top_gpas = student_gpa_sorted[:limit]

    for student in student_data:
        if student.get("GPA") in top_gpas:
            top_student_names.append(student["Name"])

    return tuple(top_student_names)

def main():
    student_data = [
        {
            "ID": 1,
            "Name": "Alice",
            "Age": 20,
            "Major": "Computer Science",
            "GPA": 3.7
        },
        {
            "ID": 2,
            "Name": "Bob",
            "Age": 21,
            "Major": "Engineering",
            "GPA": 3.9
        },
        {
            "ID": 3,
            "Name": "Omar",
            "Age": 21,
            "Major": "Engineering",
            "GPA": 3.5
        },
        {
            "ID": 4,
            "Name": "Fadi",
            "Age": 21,
            "Major": "Engineering",
            "GPA": 4.0
        }
    ]

    student_data_2 = [
        {
            "ID": 1,
            "Name": "Mahmoud",
            "Age": 20,
            "Major": "Computer Science",
            "GPA": 3.7
        },
        {
            "ID": 2,
            "Name": "Bob",
            "Age": 21,
            "Major": "Bio",
            "GPA": 3.9
        },
        {
            "ID": 3,
            "Name": "Omar",
            "Age": 21,
            "Major": "Computer Science",
            "GPA": 3.9
        }
    ]

    while True:
        user_input = input(
            "\n1. Get Student by ID\n2. Get All Students\n3. Get Students by Major\n4. Add Student\n5. Find Common Majors\n6. Delete Student\n7. Calculate Average GPA\n8. Get Top Performers\n9. Exit\nEnter your choice: "
        )

        if user_input == '1':
            student_id = int(input("Enter the ID of the student: "))
            student = GetStudentById(student_data, student_id)
            if student:
                print("Student found:", student)
            else:
                print("Student not found.")

        elif user_input == '2':
            all_students = GetAllStudents(student_data)
            print("All students:", all_students)

        elif user_input == '3':
            major = input("Enter the major: ")
            students_by_major = GetStudentByMajor(student_data, major)
            if students_by_major:
                print("Students with major", major, ":", students_by_major)
            else:
                print("No students found with major", major)

        elif user_input == '4':
            id = input("Enter ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            major = input("Enter Major: ")
            GPA = float(input("Enter GPA: "))
            addStudent(student_data, id, name, age, major, GPA)
            print("Student added successfully.")

        elif user_input == '5':
            common_majors = CommonMajor(student_data, student_data_2)
            print("Common majors:", common_majors)

        elif user_input == '6':
            student_id = input("Enter the ID of the student to delete: ")
            student_data = delete_student(student_data, student_id)

        elif user_input == '7':
            average = Average(student_data)
            print("Average GPA:", average)

        elif user_input == '8':
            limit = int(input("Enter the number of top performers: "))
            top_performers = TopPerformances(student_data, limit)
            print("Top performers:", top_performers)

        elif user_input == '9':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

