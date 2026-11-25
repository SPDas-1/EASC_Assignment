def linear_search(marks, target):
    for i in range(len(marks)):
        if marks[i] == target:
            return i
    return -1


# Main program
marks = list(map(int, input("Enter marks separated by spaces: ").split()))
target = int(input("Enter target mark: "))

position = linear_search(marks, target)

if position != -1:
    print("Mark found at index", position)
else:
    print("Mark not found")