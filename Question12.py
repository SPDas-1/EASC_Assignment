students = [
    ("S101", "Amit", [78, 85, 91, 67]),
    ("S102", "Neha", [92, 89, 95, 90]),
    ("S103", "Ravi", [56, 64, 71, 60]),
    ("S104", "Priya", [85, 90, 84, 88])
]

# 1. Convert records into a dictionary
student_dict = {
    student_id: {"name": name, "marks": marks}
    for student_id, name, marks in students
}

# 2. Calculate total and average marks
for student_id, details in student_dict.items():
    total = sum(details["marks"])
    average = total / len(details["marks"])

    details["total"] = total
    details["average"] = average

# Display total and average
print("Student Details")
print("----------------")

for student_id, details in student_dict.items():
    print(
        student_id,
        details["name"],
        "Total =", details["total"],
        "Average =", details["average"]
    )

# Identify student with highest average
highest_student = max(
    student_dict.items(),
    key=lambda x: x[1]["average"]
)

print("\nStudent with Highest Average:")
print(highest_student[0], "-", highest_student[1]["name"])
print("Average =", highest_student[1]["average"])

# 3. Students with average marks greater than 80
above_80 = list(
    filter(
        lambda x: x[1]["average"] > 80,
        student_dict.items()
    )
)

print("\nStudents with Average > 80:")
for student_id, details in above_80:
    print(student_id, "-", details["name"])

# 4. Sort students by average in descending order
sorted_students = sorted(
    student_dict.items(),
    key=lambda x: x[1]["average"],
    reverse=True
)

print("\nStudents Sorted by Average (Descending):")
for student_id, details in sorted_students:
    print(student_id, "-", details["name"], "-", details["average"])

# 5. IDs of students who scored more than 85 in at least one subject
ids_above_85 = {
    student_id
    for student_id, details in student_dict.items()
    if any(mark > 85 for mark in details["marks"])
}

print("\nIDs with at least one mark > 85:")
print(ids_above_85)