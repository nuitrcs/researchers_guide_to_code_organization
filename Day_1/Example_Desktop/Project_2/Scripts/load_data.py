import pandas as pd
from pathlib import Path

def load_data(grades_path:str, survey_path:str) -> tuple[pd.DataFrame]:
    grades_file = Path(grades_path)
    grades_data = pd.read_csv(grades_file)

    survey_file = Path(survey_path)
    survey_data = pd.read_csv(survey_file)
    
    return grades_data, survey_data