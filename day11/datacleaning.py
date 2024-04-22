import pandas as pd
import numpy as np

# Create DataFrame with missing values
data = {'A': [1, np.nan, 3, 4, np.nan],
        'B': [5, 6, np.nan, 8, 9],
        'C': [np.nan, 12, 13, np.nan, 15]}
df = pd.DataFrame(data)

# Identify rows with missing values
rows_with_missing_values = df[df.isnull().any(axis=1)]

# Replace missing values with the mean of their respective columns
df_cleaned = df.fillna(df.mean())

print("DataFrame with missing values:")
print(df)
print("\nRows with missing values:")
print(rows_with_missing_values)
print("\nDataFrame after replacing missing values with column means:")
print(df_cleaned)


# Create DataFrame with employee names and salaries
data = {'Employee': ['Alice', 'Bob', 'Charlie', 'David'],
        'Salary': ['$50000', '$60000', '$70000', '$80000']}
df1 = pd.DataFrame(data)

# Transform all employee names to uppercase
df1['Employee'] = df1['Employee'].str.upper()

# Remove dollar sign and convert 'Salary' column to numeric data type
df1['Salary'] = df1['Salary'].str.replace('$', '').astype(float)

print("DataFrame with uppercase employee names:")
print(df1)

print("\nDataFrame with 'Salary' column converted to numeric:")
print(df1)

# Sample DataFrame with employee data
data2 = {'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank'],
        'Department': ['HR', 'Finance', 'HR', 'Finance', 'HR', 'Finance'],
        'Salary': [60000, 70000, 80000, 75000, 65000, 72000]}
df2 = pd.DataFrame(data2)

# Calculate average salary per department
average_salary_per_department = df2.groupby('Department')['Salary'].mean()

print("Average salary per department:")
print(average_salary_per_department)


