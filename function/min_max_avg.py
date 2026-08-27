def calculate(numbers):
    minimum = numbers[0]
    maximum = numbers[0]
    total = 0

    for num in numbers:
        total = total + num

        if num < minimum:
            minimum = num

        if num > maximum:
            maximum = num

    average = total / len(numbers)

    return minimum, maximum, total, average


numbers = [10, 20, 5, 40, 30]

minimum, maximum, total, average = calculate(numbers)

print("Minimum =", minimum)
print("Maximum =", maximum)
print("Sum =", total)
print("Average =", average)