import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create student performance dataset
data = {
    'StudentID': range(101, 113),
    'Gender': ['Female', 'Male', 'Female', 'Male', 'Female', 'Male', 
               'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
    'StudyHours': [5.5, 4.0, 7.0, 2.5, 6.0, 8.5, 3.5, 5.0, 7.5, 2.0, 6.0, 8.5],
    'Attendance(%)': [85, 90, 95, 70, 88, 80, 75, 85, 92, 65, 88, 80],
    'Marks': [78, 65, np.nan, 52, 84, np.nan, 60, 72, 89, 45, 84, 80]
}

df_raw = pd.DataFrame(data)
df_raw.loc[11] = df_raw.loc[10] # Duplicate row
df_raw.to_csv('student_performance.csv', index=False)

# Load CSV
df = pd.read_csv('student_performance.csv')
print(f"Shape: {df.shape}")
print(f"Missing values in Marks: {df['Marks'].isnull().sum()}")
print(f"Duplicate rows: {df.duplicated().sum()}")

# Cleaning
df = df.drop_duplicates()
df['Marks'] = df['Marks'].fillna(df['Marks'].median())
print(f"After cleaning: {df.shape}")
print()

# Correlation Matrix
print("Correlation matrix:")
print(df[['StudyHours', 'Attendance(%)', 'Marks']].corr())
print()

# Groupby Gender
print("Average Marks and Attendance by Gender:")
print(df.groupby('Gender')[['Marks', 'Attendance(%)']].mean().round(1))
print()

# Save Plots
plt.figure(figsize=(5, 4))
plt.hist(df['Marks'], bins=5, color='steelblue', edgecolor='black')
plt.savefig('marks_histogram.png')
plt.close()

plt.figure(figsize=(4, 4))
plt.boxplot(df['Marks'])
plt.savefig('marks_boxplot.png')
plt.close()

plt.figure(figsize=(5, 4))
plt.scatter(df['StudyHours'], df['Marks'], color='darkorange')
plt.savefig('studyhours_vs_marks.png')
plt.close()

print("Saved marks_histogram.png, marks_boxplot.png, studyhours_vs_marks.png")