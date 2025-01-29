
import pandas as pd

df = pd.read_csv('data.csv')

print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

print("\nFirst Five Rows of the Dataset:")
print(df.head())


print("\nSize of the Dataset:", df.size)

print("\nMissing Values in Each Column:")
print(df.isnull().sum())


print("\nSum of Numerical Columns:")
print(df.sum(numeric_only=True))

print("\nAverage of Numerical Columns:")
print(df.mean(numeric_only=True))

print("\nMinimum Values in Numerical Columns:")
print(df.min(numeric_only=True))

print("\nMaximum Values in Numerical Columns:")
print(df.max(numeric_only=True))


df.to_csv('exported_data.csv', index=False)
print("\nData has been exported to 'exported_data.csv'.")
