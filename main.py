print("Student Performance Tracker")

students = {}


def add_student():
    student = input("Enter a student name: ").strip()
    if student == "":
        return "Student cannot be empty"

    if student in students:
        return "There is a student with this name"
    else:
        students[student] = []
        return "Student added."


def add_grade():
    try:
        student = input("For which student do you want to add a grade? ")
        if student not in students:
            return "Student not found"
        else:
            grade = int(input("What grade do you want to give? "))
            if 0 < grade <= 10:
                students[student].append(grade)
                return f"grade: [{grade}] was added to the student {student}"
            else:
                return f"Please enter a grade 1-10"
    except ValueError:
        return "You need to enter number(grade)!"


def show_average():
    student = input("Enter a student name: ")
    total = 0
    count = 0
    if student not in students:
        return "Student not found"
    else:
        if students[student] == []:
            return "This student doesn't have any grades"
        else:
            for grade in students[student]:
                total += grade
                count += 1
            average = total / count
            return f"The {student} average is : {round(average, 2)}"


def show_best_student():
    best_grader = None
    best_average = 0
    for student in students:
        if not students[student]:
            continue
        total = 0

        for grade in students[student]:
            total += grade
        average = total / len(students[student])
        if average > best_average:
            best_average = average
            best_grader = student
    if best_grader == None:
        return "No students with grades"
    else:
        return f"Best student: {best_grader}, average grade: {round(best_average, 2)}"


def show_statistics():
    if students == {}:
        return "Students not found"
    else:
        for student in students:
            average = 0
            if students[student] == []:
                print(f"Student: {student} - no grades")
            else:
                average = sum(students[student]) / len(students[student])
                print(
                    f"Student: {student} - Grades: {students[student]} - Average: {round(average, 2)}")


while True:
    try:
        menu = int(input(
            "1. Add student\n"
            "2. Add grade\n"
            "3. Get average grade\n"
            "4. Show best student\n"
            "5. Show statistics\n"
            "6. Exit\n"



        ))
        if menu == 1:
            print(add_student())
        elif menu == 2:
            print(add_grade())
        elif menu == 3:
            print(show_average())
        elif menu == 4:
            print(show_best_student())
        elif menu == 5:
            result = show_statistics()
            if result:
                print(result)
        elif menu == 6:
            break
    except ValueError:
        print("Enter a number!")
