import pandas as pd

def aggregate_data(grades_data: pd.DataFrame, survey_data: pd.DataFrame) -> pd.DataFrame:
    # Average hw and exams
    final_data = survey_data.copy()
    final_data["Average_HW"] = grades_data[[f"Homework {n+1}" for n in range(5)]].mean(axis=1)
    final_data["Average_Exams"] = grades_data[["Exam 1", "Exam 2"]].mean(axis=1)

    return final_data