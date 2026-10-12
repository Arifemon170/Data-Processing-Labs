marks=[45,57,89,65]
print(f"total marks{sum(marks)}")
print(f"average marks{sum(marks)/len(marks)}")
print(f"highest mark:{max(marks)}")
print(f"lowest mark:{min(marks)}")
count=0
for x in marks:
    if x>=50:
        count+=1
print(f"no of passed students{count}")

