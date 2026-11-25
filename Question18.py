class Student:
    def __init__(self, student_id, name, attendance, marks):
        self.student_id = student_id
        self.name = name
        self.attendance = attendance
        self.marks = marks

    # Calculate average attendance percentage
    def average_attendance(self):
        total_attended = sum(self.attendance.values())
        total_classes = len(self.attendance) * 30
        return (total_attended / total_classes) * 100

    # Calculate average marks
    def average_marks(self):
        return sum(self.marks) / len(self.marks)

    # Check whether attendance is at least 75% in every subject
    def attendance_75_every_subject(self):
        return all(
            (classes / 30) * 100 >= 75
            for classes in self.attendance.values()
        )


# Create multiple Student objects
students = [
    Student(
        "S101",
        "Amit",
        {"Python": 26, "DBMS": 23, "OS": 28},
        (82, 76, 91)
    ),

    Student(
        "S102",
        "Neha",
        {"Python": 28, "DBMS": 27, "OS": 29},
        (92, 88, 95)
    ),

    Student(
        "S103",
        "Ravi",
        {"Python": 20, "DBMS": 24, "OS": 22},
        (68, 74, 70)
    ),

    Student(
        "S104",
        "Priya",
        {"Python": 25, "DBMS": 26, "OS": 27},
        (85, 90, 88)
    )
]


# Display average attendance and marks
print("Student Performance")
print("-------------------")

for student in students:
    print(
        student.student_id,
        "-", student.name,
        "| Average Attendance =",
        round(student.average_attendance(), 2), "%",
        "| Average Marks =",
        round(student.average_marks(), 2)
    )


# 1. Students having at least 75% attendance in every subject
eligible_students = list(
    filter(
        lambda student: student.attendance_75_every_subject(),
        students
    )
)

print("\nStudents with at least 75% attendance in every subject:")
for student in eligible_students:
    print(student.student_id, "-", student.name)


# 2. Rank students according to average marks
ranked_students = sorted(
    students,
    key=lambda student: student.average_marks(),
    reverse=True
)

print("\nStudents Ranked by Average Marks:")
for rank, student in enumerate(ranked_students, start=1):
    print(
        rank,
        ".",
        student.student_id,
        "-",
        student.name,
        "-",
        round(student.average_marks(), 2)
    )


# 3. Dictionary: subject -> set of students with >= 75% attendance
subject_attendance = {}

for subject in ["Python", "DBMS", "OS"]:
    subject_attendance[subject] = {
        student.student_id
        for student in students
        if (student.attendance[subject] / 30) * 100 >= 75
    }

print("\nStudents with at least 75% attendance in each subject:")
print(subject_attendance)


# 4. IDs satisfying both conditions:
# Average marks >= 80 AND average attendance >= 75%
qualified_ids = tuple(
    student.student_id
    for student in students
    if student.average_marks() >= 80
    and student.average_attendance() >= 75
)

print("\nStudents satisfying both conditions:")
print(qualified_ids)