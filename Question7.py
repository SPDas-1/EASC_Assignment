# Input number of rows
N = int(input("Enter the number of rows: "))

# Nested loops to display sensor arrangement
for i in range(1, N + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()