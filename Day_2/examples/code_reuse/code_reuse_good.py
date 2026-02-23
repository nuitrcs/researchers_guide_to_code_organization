student_data = [
    {"name": "Alice", "scores": [85, 90, 98]},
    {"name": "Bo", "scores": [70, 82, 88]},
    {"name": "Citlali", "scores": [95, 92, 99]}
]

# function to be reused
def calculate_grade(student_name, student_scores):
    average = sum(student_scores) / len(student_scores)
    message = f"Student: {student_name} | Grade: + {average}"
    return message

# loop
for student in student_data:
    print(calculate_grade(student["name"], student["scores"]))