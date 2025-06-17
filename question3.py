import pandas as pd
data = {
    'Name': ['John', 'Emma', 'Alice', 'Bob'],
    'Math': [88, 92, 74, 61],
    'Physics': [79, 85, 90, 55],
    'Chemistry': [90, 70, 68, 49]
}
df = pd.DataFrame(data)
df['Total'] = df[['Math', 'Physics', 'Chemistry']].sum(axis=1)
df['Percentage'] = (df['Total'] / 3).round(2)
def get_grade(p):
    if p >= 90:
        return 'A'
    elif p >= 75:
        return 'B'
    elif p >= 60:
        return 'C'
    elif p >= 50:
        return 'D'
    else:
        return 'F'
df['Grade'] = df['Percentage'].apply(get_grade)
print("Student DataFrame:")
print(df)
print("\nStudents with Percentage >= 70:")
print(df[df['Percentage'] >= 70])
