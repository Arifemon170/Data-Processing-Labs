
students = [
    {"name": "Arif", "department": "CSE", "marks": 85, "attendance": 90},
    {"name": "Rahim", "department": "EEE", "marks": 72, "attendance": 75},
    {"name": "Karim", "department": "CSE", "marks": 92, "attendance": 95},
    {"name": "Nila", "department": "Physics", "marks": 68, "attendance": 70},
    {"name": "Sara", "department": "CSE", "marks": 78, "attendance": 85}
]

def average_marks(students):
    total = 0

    for student in students:
        total += student["marks"]

    return total / len(students)

def highest_marks(students):
    highest = students[0]

    for student in students:
        if student["marks"] > highest["marks"]:
            highest = student

    return highest
def low_attendance(students):
    count = 0

    for student in students:
        if student["attendance"] < 80:
            count += 1

    return count

average = average_marks(students)
top_student = highest_marks(students)
low_count = low_attendance(students)

print("Average marks:", average)
print("Highest-scoring student:", top_student["name"])
print("Highest marks:", top_student["marks"])
print("Students with attendance below 80%:", low_count)
