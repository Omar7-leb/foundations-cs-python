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

def get_youngest_student(students):
    youngest = 100
    for student in students:
        if student['age'] < youngest:
            youngest = student['age']
            youngest_name = student['name']
    return youngest_name

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

def add_student(students):
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    scores = tuple(map(int, input("Enter three exam scores separated by spaces: ").split()))
    new_student = {"name": name, "age": age, "Scores": scores}
    students.append(new_student)

def delete_student(students, name_to_delete):
    updated_students = [student for student in students if student['name'] != name_to_delete]
    if len(updated_students) == len(students):
        print("Student not found!")
    else:
        print(f"{name_to_delete} was deleted successfully.")
    return updated_students