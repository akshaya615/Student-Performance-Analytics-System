# 1. 🎓 Student Performance Analytics System

📊 A Python-based data analytics project to evaluate student marks, calculate grades, analyze attendance, and compare academic performance across subjects and departments.

## 1.1. 📌 Project Overview

The **Student Performance Analytics System** analyzes student marks and attendance using **Python, Pandas, and NumPy**. It transforms student records into useful summaries that make it easier to understand individual and overall class performance.

The system calculates totals and averages, assigns grades, determines pass/fail results, identifies top-performing students, compares subject-wise and department-wise averages, and flags students with attendance below 75%.

## 1.2. 🎯 Objectives

* 🗂️ Store and analyze student academic records.
* ➕ Calculate total and average marks.
* 🏅 Assign grades based on average marks.
* ✅ Determine pass/fail results.
* 📈 Identify the highest- and lowest-performing students.
* 📚 Compare subject-wise and department-wise averages.
* 🥇 Display the top five students.
* 🕒 Identify students with attendance below 75%.

## 1.3. 🛠️ Technologies Used

| Technology | Purpose |
|----|----|
| Python 3.8.10 | Core programming language |
| Pandas | Data loading, filtering, sorting, and analysis |
| NumPy | Numerical calculations |
| CSV | Stores the student dataset |
| Visual Studio Code | Development environment |
| Git and GitHub | Version control and project hosting |

## 1.4. 🗃️ Dataset Description

The project uses a CSV file named `students.csv` containing **20 student records**.

| Column | Description |
|----|----|
| `Student_ID` | Unique student identifier |
| `Name` | Student name |
| `Department` | Student's department |
| `Python` | Python marks |
| `SQL` | SQL marks |
| `Maths` | Mathematics marks |
| `Attendance` | Attendance percentage |

## 1.5. 🏗️ Project Structure

```text
Student_Performance_Analytics/
│
├── main.py              # Main program and analysis
├── students.csv         # Student marks and attendance data
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── .gitignore           # Files Git should ignore
└── screenshots/         # Program output screenshots
```

## 1.6. ⚙️ Features

### 1.6.1. 🗂️ Student Data Management

Loads `students.csv` into a Pandas DataFrame and displays student records for analysis.

### 1.6.2. ➕ Total and Average Marks

Calculates each student's total marks across Python, SQL, and Maths, then calculates the average.

**Formulas:**

* Total Marks = Python + SQL + Maths
* Average Marks = Total Marks / 3

### 1.6.3. 🏅 Grade Calculation

Assigns a grade according to the student's average marks.

| Average Marks | Grade |
|----|----|
| 90 and above | A |
| 80 to below 90 | B |
| 70 to below 80 | C |
| 60 to below 70 | D |
| Below 60 | F |

### 1.6.4. ✅ Pass/Fail Analysis

* **Pass:** Average marks are at least 40.
* **Fail:** Average marks are below 40.

### 1.6.5. 📊 Class Performance Summary

Displays the overall class average and identifies the highest- and lowest-performing students.

### 1.6.6. 📚 Subject-Wise Analysis

Calculates the average marks for Python, SQL, and Maths and identifies the subject with the highest average.

### 1.6.7. 🥇 Top Five Students

Sorts students by average marks and displays the five highest-performing students.

### 1.6.8. 🕒 Attendance Analysis

Calculates average attendance and lists students whose attendance is below **75%**.

### 1.6.9. 🏢 Department-Wise Analysis

Calculates average marks for each department and identifies the department with the highest average.

## 1.7. 🚀 Installation and Execution

### 1.7.1. Prerequisites

* Python 3.8.10 or a compatible Python installation
* Visual Studio Code (recommended)
* A terminal or command prompt
* Git (if cloning the repository)

### 1.7.2. Clone the Repository

Replace the URL with your actual GitHub repository URL.

```bash
git clone https://github.com/akshaya615/Student-Performance-Analytics-System.git
cd student-performance-analytics-system
```

### 1.7.3. Install Dependencies

Run the following command in the project folder:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should contain:

```text
pandas==2.0.3
numpy==1.24.4
```

### 1.7.4. Run the Program

```bash
python main.py
```

The program reads `students.csv`, performs the analysis, and displays the results in the terminal.

## 1.8. 📺 Expected Output

When the program runs, it displays:

* 📋 Student records
* ➕ Total and average marks
* 🏅 Grades and pass/fail results
* 📊 Class performance summary
* 📚 Subject-wise averages
* 🥇 Top five students
* 🕒 Average attendance and students below the 75% threshold
* 🏢 Department-wise averages

### 1.8.1. 📸 Screenshots

Screenshots of   program output are in  the `screenshots/` folder.

screenshots:


1. Student records
2. Marks, averages, and grades
3. Pass/fail results and class summary
4. Subject-wise analysis and top five students
5. Attendance analysis
6. Department-wise performance

## 1.9. 🧠 Learning Outcomes

* 🐍 Python functions, conditional statements, and loops
* 🐼 Pandas DataFrames and data manipulation
* 🔢 NumPy numerical operations
* 📄 CSV file handling
* 📊 Sorting, filtering, aggregation, and data analysis
* 🌿 GitHub repository organization and project documentation

## 1.10. 🧩 Challenges and Solutions

| Challenge | Solution |
|----|----|
| Organizing student records for analysis | Stored records in a CSV file and loaded them using Pandas |
| Repeating calculations across students and subjects | Used reusable functions, Pandas operations, and loops |
| Identifying top performers and low-attendance students | Used sorting, aggregation, and filtering operations |
| Comparing academic performance across departments | Used Pandas `groupby()` to calculate department averages |

## 1.11. ⚠️ Limitations

* The project analyzes only the data provided in the sample dataset.
* The accuracy of the results depends on the correctness and completeness of student marks and attendance.
* The grading and pass/fail criteria are predefined.
* The current dataset contains 20 student records; results may differ with a larger dataset.
* The program displays results in the terminal and does not include a graphical user interface.

## 1.12. 🔮 Future Enhancements

Possible future improvements include:

* Adding more subjects and student records
* Generating charts and visual reports
* Exporting analysis results to CSV or Excel
* Connecting the project to a database
* Developing a graphical user interface

These are possible extensions and are not part of the current implementation.

## 1.13. 🎓 Conclusion

The **Student Performance Analytics System** demonstrates how Python, Pandas, and NumPy can be used to analyze academic records and produce meaningful summaries. It brings together grade calculation, pass/fail analysis, class and subject comparisons, department analysis, top-student identification, and attendance monitoring in one project.

This project provides a practical foundation for further learning in data analysis and student performance reporting.

## 1.14. 📚 References

* [Python Documentation](https://docs.python.org/3/)
* [Pandas Documentation](https://pandas.pydata.org/docs/)
* [NumPy Documentation](https://numpy.org/doc/)

## 1.15. 🔗 GitHub Repository

**Repository URL:** `https://github.com/akshaya615/Student-Performance-Analytics-System`