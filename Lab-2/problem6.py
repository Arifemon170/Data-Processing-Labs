def calculate_grade(marks):
    avg = sum(marks) / len(marks)

    if avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


marks = [85, 75, 90, 80, 70]
grade = calculate_grade(marks)

print("Average:", sum(marks) / len(marks))
print("Grade:", grade)