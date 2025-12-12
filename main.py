from pathlib import Path
import csv
import json

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
#  Compute average
total_score = sum(student["score"] for student in students)
average_score = total_score / len(students)
print("Class average:", average_score)

#  Save average to JSON
average_path = Path("data/average.json")

average_data = {"average_score": average_score}
average_path.write_text(json.dumps(average_data, indent=4))

#  Generate TXT summary
summary_path = Path("data/summary.txt")

# Find top student
top_student = max(students, key=lambda x: x["score"])

# Create summary text
summary_text = (
    f"Top student: {top_student['name']} ({top_student['score']})\n"
    f"Class average: {average_score}\n"
    f"Total students: {len(students)}"
)

# Write summary to TXT
summary_path.write_text(summary_text)
