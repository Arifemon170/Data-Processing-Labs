name = input("Enter student's name: ")

marks = []

for i in range(5):
    mark = float(input(f"Enter mark for course {i + 1}: "))
    marks.append(mark)

total = sum(marks)
average = total / 5
highest = max(marks)
lowest = min(marks)

passed = 0

for mark in marks:
    if mark >= 50:
        passed += 1

if average >= 80:
    performance = "Excellent"
elif average >= 70:
    performance = "Good"
elif average >= 60:
    performance = "Satisfactory"
elif average >= 50:
    performance = "Pass"
else:
    performance = "Needs Improvement"

print("\n--- Student Performance ---")
print("Name:", name)
print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Passed courses:", passed)
print("Performance:", performance)
