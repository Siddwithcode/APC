def unique_elements(numbers):
    unique = []

    for num in numbers:
        if num not in unique:
            unique.append(num)

    return unique


numbers = [10, 20, 10, 30, 20, 40]

print("Unique elements =", unique_elements(numbers))