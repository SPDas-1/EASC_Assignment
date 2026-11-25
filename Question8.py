# Input the number of rows
N = int(input("Enter the value of N: "))

# Generate the pattern using nested loops
for i in range(1, N + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()