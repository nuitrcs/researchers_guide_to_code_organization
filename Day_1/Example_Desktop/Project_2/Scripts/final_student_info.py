from aggregate_data import aggregate_data
from load_data import load_data

# Get raw data
survey_data_file = "Data/Raw/student_final_survey.csv"
grades_data_file = "Data/Raw/student_grades.csv"
grades, surveys = load_data(grades_data_file, survey_data_file)

# Aggregate data
student_final_info = aggregate_data(grades, surveys)

# Print
for student in student_final_info.itertuples():
    print(f"{student.Name}'s information:\nHW Grade: {student.Average_HW}\nExam Grade: {student.Average_Exams}\nFavorite Animal: {student.Favorite_Animal}\nFeedback: {student.Feedback}\n")