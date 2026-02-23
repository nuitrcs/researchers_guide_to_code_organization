# imports
from load_data import load_student_grades, load_student_survey
from preprocess_data import get_column_average
from analysis import get_final_score, rank_students
from visualization import plot_final_grades, plot_effort_vs_performance


# step 1: load the data
grades_path = 'Day_2/examples/modularity/Data/student_grades.csv'
survey_path = 'Day_2/examples/modularity/Data/student_final_survey.csv'

grades = load_student_grades(grades_path)
survey = load_student_survey(survey_path)

# step 2: preprocess data
hw_columns = [f"Homework {n+1}" for n in range(5)]
exam_columns = ["Exam 1", "Exam 2"]

hw_avg = get_column_average(grades, hw_columns)
exam_avg = get_column_average(grades, exam_columns)

final_df = survey.copy()
final_df['hw_average'] = hw_avg
final_df['exam_average'] = exam_avg

# step 3: analyze
final_df['Final Score'] = get_final_score(final_df, 'hw_average', 'exam_average', .7) # weighted average
ranked_students = rank_students(final_df)

print(f"Top Students: {ranked_students.head(3)}")


# step 4: visualize
plot_final_grades(final_df)
plot_effort_vs_performance(final_df)