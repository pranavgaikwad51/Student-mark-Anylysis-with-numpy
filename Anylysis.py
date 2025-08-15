import numpy as np
import pandas as pd

# Load dataset
df = pd.read_csv("students.csv")
print("Original Data:\n", df)


marks = df[['math', 'science', 'english']].to_numpy()

# Calculate total marks per student
total_marks = np.sum(marks, axis=1)
df['total'] = total_marks


avg_per_subject = np.mean(marks, axis=0)   # Calculating average mark

# Calculate student with highest and lowest total marks
max_score = np.max(total_marks)
min_score = np.min(total_marks)
top_student = df.iloc[np.argmax(total_marks)]['name']
bottom_student = df.iloc[np.argmin(total_marks)]['name']

# Filter students who scored above 80 in all subjects
high_achievers = df[(df['math'] > 80) & (df['science'] > 80) & (df['english'] > 80)]

print("\nAverage Marks per Subject:", avg_per_subject)
print(f"Top Student: {top_student} ({max_score} marks)")
print(f"Lowest Student: {bottom_student} ({min_score} marks)")
print("\nHigh Achievers:\n", high_achievers)
