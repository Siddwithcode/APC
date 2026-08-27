def average(numbers):
    total = 0

    for num in numbers:
        total = total + num

    return total / len(numbers)


numbers = [10, 20, 30, 40, 50]

print("Average =", average(numbers))