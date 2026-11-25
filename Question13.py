employees = [
    ("E101", "Alice", "IT", 65000),
    ("E102", "Bob", "HR", 52000),
    ("E103", "Charlie", "IT", 78000),
    ("E104", "David", "Finance", 72000),
    ("E105", "Eva", "IT", 85000)
]

# a. Create department-wise dictionary of employee IDs
department_employees = {}

for emp_id, name, department, salary in employees:
    if department not in department_employees:
        department_employees[department] = set()

    department_employees[department].add(emp_id)

print("Department-wise Employee IDs:")
print(department_employees)

# b. Find highest-paid employee and average salary
highest_paid = max(employees, key=lambda x: x[3])
average_salary = sum(emp[3] for emp in employees) / len(employees)

print("\nHighest-Paid Employee:")
print(highest_paid[1], "-", highest_paid[3])

print("Average Salary:", average_salary)

# c. Employees earning more than ₹70,000
high_salary = list(
    filter(lambda x: x[3] > 70000, employees)
)

print("\nEmployees earning more than ₹70,000:")
for employee in high_salary:
    print(employee)

# d. Sort employees by salary in descending order
sorted_employees = sorted(
    employees,
    key=lambda x: x[3],
    reverse=True
)

print("\nEmployees Sorted by Salary:")
for employee in sorted_employees:
    print(employee)

# e. IT employees earning more than ₹70,000
it_employees = department_employees["IT"]

it_high_salary = [
    employee
    for employee in employees
    if employee[0] in it_employees and employee[3] > 70000
]

print("\nIT Employees earning more than ₹70,000:")
for employee in it_high_salary:
    print(employee)