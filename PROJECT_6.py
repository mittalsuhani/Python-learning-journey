#project 6 is a student marks manager
#it uses basic concepts of dictionaries and grading logic

def calculate_percentage(marks, total_marks):
    if(marks<0 or marks>100):
        return "Invalid Marks"
    return (marks / total_marks) * 100

def calculate_grade(marks):
    if(marks<0 or marks>100):
        return "Invalid Marks"
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'
    

student_marks = {}    # Dictionary to store student names and their marks
num_students = int(input("Enter number of students: "))
    
    # Collecting student names and their marks
for i in range(num_students):
        name = input("Enter student name: ")
        marks = float(input(f"Enter marks for {name} (out of 100): "))
        student_marks[name] = marks
    
    # Displaying student grades
print("\nStudent Grades:")
for name, marks in student_marks.items():
        grade = calculate_grade(marks)
        percent=calculate_percentage(marks, 100)
        print(f"{name}: Marks = {marks}, Grade = {grade},Percentage = {percent:.2f}%")