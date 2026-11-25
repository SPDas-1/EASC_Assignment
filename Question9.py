# Read the list of integers
numbers = list(map(int, input("Enter integers separated by spaces: ").split()))

found = False

# Search for the first repeated element
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            print("First repeated element:", numbers[i])
            print("Second-occurrence position:", j)
            found = True
            break

    if found:
        break

# If no repeated element is found
if not found:
    print("No repeated element")