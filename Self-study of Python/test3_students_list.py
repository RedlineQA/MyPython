while True:
    try:
        student_num = int(input("Enter the number of students in the class: "))
        if student_num > 0:
            break
        else:
            print("The number must be greater than 0.")
    except ValueError:
        print("The number must be an integer.")
students = []
for i in range(student_num):
    student = input("Enter the student's name: ")
    grades = input("Enter grades (comma separated)")
    students.append((student, grades))
print("\n--- Results ---")
for i, (student, grades) in enumerate(students, 1):
    grade_list = grades.split(",")
    grades_int = [int(grade.strip()) for grade in grade_list]
    average = sum(grades_int) / len(grades_int)
    print(f"{i}. {student}")
    print(f"   Grades: {grades}")
    print(f"   Average: {average:.2f}")
    if average >= 90:
        print("   🏆 Excellent!")
    elif average < 60:
        print("   ❗ Needs improvement")
