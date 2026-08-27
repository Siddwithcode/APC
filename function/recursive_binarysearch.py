def binary_search(numbers, low, high, target):

    if low > high:
        return -1

    middle = (low + high) // 2

    if numbers[middle] == target:
        return middle

    elif target < numbers[middle]:
        return binary_search(numbers, low, middle - 1, target)

    else:
        return binary_search(numbers, middle + 1, high, target)


numbers = [10, 20, 30, 40, 50, 60, 70]

target = int(input("Enter number to search: "))

result = binary_search(numbers, 0, len(numbers) - 1, target)

if result == -1:
    print("Element not found")
else:
    print("Element found at index", result)