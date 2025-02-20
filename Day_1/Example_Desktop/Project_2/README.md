# Student Grades and Survey Processor

This project loads student data from CSV files, calculates their average homework and exam grades, and prints the results along with their feedback and favorite animal.

## Project Overview

The Jupyter notebook `final_student_info.py` performs the following tasks:
1. **Loads Grades Data:** It reads a CSV file containing student names and their respective homework and exam grades.
2. **Loads Survey Data:** It reads a second CSV file containing the students' feedback about the course and their favorite animal.
3. **Calculates Averages:** The script computes the average grade across homework assignments and exams for each student.
4. **Prints Results:** For each student, the script prints:
   - Their name
   - Average homework grade
   - Average exam grade
   - Favorite mythical creature
   - Feedback on the course

## Directory Structure
The project expects the data files to be in the following structure:
```
/Project Root
  ├── /Data
      ├── /Raw
          ├── student_grades.csv
          └── student_final_survey.csv
      └── /Processed
          └── student_survey_and_final_grades.csv
  ├── /Exploration
      └── process_grades.ipynb
  ├── /Scripts
      ├── aggregate_data.py
      ├── final_student_info.py
      └── load_data.py
  └── README.md
```

- **`student_grades.csv`**: Contains student names, homework grades, and exam grades.
- **`student_final_survey.csv`**: Contains student names, course feedback, and their favorite animal.

## How to Use

1. Make sure you have the CSV files in the correct directory (`/Data/Raw/`).
2. Make sure your current working directory is `Project_2`.
2. Run the python script (`final_student_info.py`)
```bash
python Scripts/final_student_into.py
```
3. The script will print each student's average homework grade, average exam grade, feedback, and favorite animal.

## Example Output

Here is an example of what the output might look like:
```
Ares's information:
HW Grade: 73.4
Exam Grade: 82.5
Favorite Animal: Centaur
Feedback: Prof. efrén's class could use more battle simulations.

Artemis's information:
HW Grade: 94.6
Exam Grade: 93.0
Favorite Animal: Deer
Feedback: Loved it! efrén's explanations were straight like an arrow.

...
```

## Requirements

- Python 3.x
- `pandas` library

You can install the required library with:
```bash
pip install pandas
```