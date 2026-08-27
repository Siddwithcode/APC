def count_element(numbers, element):
    count = 0

    for num in numbers:
        if num == element:
            count = count + 1

    return count


numbers = [10, 20, 10, 30, 10, 40]

element = int(input("Enter element to search: "))

print("Occurrences =", count_element(numbers, element))