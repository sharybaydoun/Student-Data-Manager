from pathlib import Path
import csv

# Path to the CSV file
students_path = Path("data/students.csv")

# Read CSV as dictionaries
students = []  # to store all student records
with students_path.open("r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Convert score to int before storing
        row["score"] = int(row["score"])
        students.append(row)

# Print to check
for s in students:
    print(s)
