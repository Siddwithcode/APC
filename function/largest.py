def largest(numbers):
    large = numbers[0]

    for num in numbers:
        if num > large:
            large = num

    return large


numbers = [10, 25, 5, 40, 15]

print("Largest number =", largest(numbers))