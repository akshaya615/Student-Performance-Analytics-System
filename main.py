
import pandas as pd
import numpy as np

# Load the student dataset
students = pd.read_csv("students.csv")

# Display the complete dataset
print("\n===== STUDENT PERFORMANCE ANALYTICS SYSTEM =====")
print("\nStudent Records:")
print(students.to_string(index=False))

# Display basic dataset information
print("\nTotal Number of Students:", len(students))
print("\nDepartment Names:")
print(students["Department"].unique())

# Calculate total marks for each student
students["Total_Marks"] = (
    students["Python"] +
    students["SQL"] +
    students["Maths"]
)

# Calculate average marks for each student
students["Average_Marks"] = (
    students["Total_Marks"] / 3
)

# Display student performance
print("\n===== STUDENT MARKS ANALYSIS =====")

print(
    students[
        ["Name", "Department", "Total_Marks", "Average_Marks"]
    ].to_string(index=False)
)

# Function to assign grades
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


# Apply the function to every student
students["Grade"] = students["Average_Marks"].apply(calculate_grade)

# Display student grades
print("\n===== STUDENT GRADES =====")
print(students[["Name", "Average_Marks", "Grade"]].to_string(index=False))

# Function to determine pass or fail
def calculate_result(average):
    if average >= 40:
        return "Pass"
    else:
        return "Fail"


# Apply the function to all students
students["Result"] = students["Average_Marks"].apply(calculate_result)

# Display pass/fail results
print("\n===== STUDENT PASS/FAIL RESULTS =====")
print(
    students[["Name", "Average_Marks", "Result"]].to_string(index=False)
)

# Count passed and failed students
passed = (students["Result"] == "Pass").sum()
failed = (students["Result"] == "Fail").sum()

print("\nTotal Passed Students:", passed)
print("Total Failed Students:", failed)

# Class Performance Summary
print("\n===== CLASS PERFORMANCE SUMMARY =====")

# Calculate overall class average
class_average = np.mean(students["Average_Marks"])

# Find the highest-performing student
highest_index = students["Average_Marks"].idxmax()
highest_student = students.loc[highest_index, "Name"]
highest_average = students.loc[highest_index, "Average_Marks"]

# Find the lowest-performing student
lowest_index = students["Average_Marks"].idxmin()
lowest_student = students.loc[lowest_index, "Name"]
lowest_average = students.loc[lowest_index, "Average_Marks"]

# Display the summary
print("Overall Class Average:", round(class_average, 2))
print("Highest Performing Student:", highest_student)
print("Highest Average Marks:", round(highest_average, 2))
print("Lowest Performing Student:", lowest_student)
print("Lowest Average Marks:", round(lowest_average, 2))

# Subject-Wise Performance Analysis
print("\n===== SUBJECT-WISE PERFORMANCE ANALYSIS =====")

subjects = ["Python", "SQL", "Maths"]

subject_averages = {}

for subject in subjects:
    average = np.mean(students[subject])
    subject_averages[subject] = average
    print(subject, "Average Marks:", round(average, 2))

# Find the best-performing subject
best_subject = max(subject_averages, key=subject_averages.get)

print("\nBest Performing Subject:", best_subject)
print(
    "Highest Subject Average:",
    round(subject_averages[best_subject], 2)
)

# Top 5 Performing Students
print("\n===== TOP 5 PERFORMING STUDENTS =====")

top_students = students.sort_values(
    by="Average_Marks",
    ascending=False
).head(5)

print(
    top_students[
        ["Name", "Department", "Average_Marks", "Grade"]
    ].to_string(index=False)
)


# Attendance Analysis
print("\n===== ATTENDANCE ANALYSIS =====")

# Calculate average attendance
average_attendance = np.mean(students["Attendance"])

print("Overall Average Attendance:", round(average_attendance, 2), "%")

# Identify students with attendance below 75%
low_attendance = students[students["Attendance"] < 75]

print("\nStudents with Attendance Below 75%:")

if len(low_attendance) > 0:
    print(
        low_attendance[["Name", "Department", "Attendance"]]
        .to_string(index=False)
    )
else:
    print("No students have attendance below 75%.")

print("\nTotal Students with Low Attendance:", len(low_attendance))

# Department-Wise Performance Analysis
print("\n===== DEPARTMENT-WISE PERFORMANCE =====")

department_average = students.groupby("Department")["Average_Marks"].mean()

for department, average in department_average.items():
    print(department, "Average Marks:", round(average, 2))

# Find the best-performing department
best_department = department_average.idxmax()

print("\nBest Performing Department:", best_department)
print(
    "Department Average Marks:",
    round(department_average[best_department], 2)
)

