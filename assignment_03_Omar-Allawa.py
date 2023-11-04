#FSD
#1-----------------------------------
def calculate_average(Scores):
    return sum(Scores) / len(Scores)

def calculate_average_scores(students):
    student_average_dict = {}
    for student in students:
        name = student['name']
        scores = student['Scores']
        average = round(calculate_average(scores), 2)
        student_average_dict[name] = average
    return student_average_dict
#2--------------------------------
def get_youngest_student(students):
    youngest = 100
    for student in students:
        if student['age'] < youngest:
            youngest = student['age']
            youngest_name = student['name']
    return youngest_name
#3--------------------------------
def calculate_total_score(scores):
    return sum(scores)

def get_highest_score(students):
    highest_score = -1
    highest_score_name = None
    for student in students:
        total_score = calculate_total_score(student['Scores'])
        if total_score > highest_score:
            highest_score = total_score
            highest_score_name = student['name']
    return highest_score_name
#4--------------------------------
def add_student(students):
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    scores = tuple(map(int, input("Enter three exam scores separated by spaces: ").split()))
    new_student = {"name": name, "age": age, "Scores": scores}
    students.append(new_student)
#5--------------------------------
def delete_student(students, name_to_delete):
    updated_students = [student for student in students if student['name'] != name_to_delete]
    if len(updated_students) == len(students):
        print("Student not found!")
    else:
        print(f"{name_to_delete} was deleted successfully.")
    return updated_students
#6--------------------------------
def common_students(students, students2):
    common = []
    for student in students:
        for student2 in students2:
            if student['name'] == student2['name']:
                common.append(student['name'])
    return common
#7-------------------------------------
def consistent_improvement_students(students):
    consistent_students = []
    for student in students:
        score = student['Scores']
        if score[0] < score[1] < score[2]:
            consistent_students.append(student['name'])
    return tuple(consistent_students)

def main():
    students = [
        {"name": "John", "age": 20, "Scores": (85, 90, 95)},
        {"name": "Alice", "age": 22, "Scores": (78, 92, 96)},
        {"name": "Bob", "age": 18, "Scores": (95, 88, 79)},
        {"name": "Omar", "age": 22, "Scores": (95, 88, 79)}
    ]
    students2 = [
        {"name": "John", "age": 20, "Scores": (85, 90, 75)},
        {"name": "Bob", "age": 18, "Scores": (95, 88, 79)},
        {"name": "Fadi", "age": 19, "Scores": (70,50,90)}
    ]

    while True:
        user_input = input("\n1. Get Average Score\n2. Get Youngest Student\n3. Get Highest Score\n4. Add Student\n5. Delete Student\n6. Get Common Students\n7. Find Students with Consistent Improvement\n8. Exit\nEnter your choice: ")

        if user_input == '1':
            average_scores_dict = calculate_average_scores(students)
            print("The average of the students:", average_scores_dict)
        elif user_input == '2':
            youngest_student_name = get_youngest_student(students)
            print("The youngest student is:", youngest_student_name)
        elif user_input == '3':
            highest_score_name = get_highest_score(students)
            print("The student with the highest score is:", highest_score_name)
        elif user_input == '4':
            add_student(students)
            print("Student added successfully.")
        elif user_input == '5':
            name_to_delete = input("Enter the name of the student to delete: ")
            students = delete_student(students, name_to_delete)
        elif user_input == '6':
            common_students_list = common_students(students, students2)
            print("The common students are:", common_students_list)
        elif user_input == '7':
            students_with_improvement = consistent_improvement_students(students)
            print("Students with consistent improvement:", students_with_improvement)
        elif user_input == '8':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
