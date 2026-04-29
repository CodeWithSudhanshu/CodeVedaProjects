import pandas as pd

# Load dataset
df = pd.read_csv("data/1) iris.csv")

# Show first 5 rows
print("First 5 Rows:")
print(df.head())

# Show shape
print("\nShape:")
print(df.shape)

# Show column names
print("\nColumns:")
print(df.columns)

# Show info
print("\nInfo:")
df.info()

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Save cleaned dataset
df.to_csv("data/cleaned/cleaned_iris.csv", index=False)

print("\nCleaned file saved successfully!")