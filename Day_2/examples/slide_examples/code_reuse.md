```bash
# Student 1: Alice
total_1 ← 85 + 90 + 88
average_1 ← total_1 / 3
print("Student: Alice | Grade: " + average_1)

# Student 2: Bo
total_2 ← 70 + 82 + 88
average_2 ← total_2 / 3
print("Student: Bo | Grade: " + average_2)

# Student 3: Citlali
total_3 ← 95 + 92 + 99
average_3 ← total_2 / 3 
print("Student: Citlali | Grade: " + average_3)
```

```bash
# data
student_data ←
    {"name": "Alice", "scores": [85, 90, 98]},
    {"name": "Bo", "scores": [70, 82, 88]},
    {"name": "Citlali", "scores": [95, 92, 99]}

# function to be reused
function calculate_grade(student_name, student_scores):
    average ← sum(student_scores) / len(student_scores)
    message ← "Student: " + student_name + " | Grade: " + average
    return message
END function 

# loop
for EACH student IN student_data:
    print(calculate_grade(student["name"], student["scores"]))
END for
```