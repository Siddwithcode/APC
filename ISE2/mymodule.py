def total(marks):
    return sum(marks)


def percentage(marks):
    return sum(marks) / len(marks)


def grade(per):
    if per > 90:
        return "A Grade"
    elif per >= 70:
        return "B Grade"
    else:
        return "C Grade"