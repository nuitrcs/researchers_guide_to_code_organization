import pandas as pd

def load_student_grades(grades_path):
    grades = pd.read_csv(grades_path)
    return grades

def load_student_survey(survey_path):
    survey = pd.read_csv(survey_path)
    return survey