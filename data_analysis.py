import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/processed/cleaned_dataset.csv")

# Summary statistics
print("Summary Statistics:")
print(df.describe())

# Example: Count of unique values in a categorical column (if exists)
for col in df.select_dtypes(include='object').columns:
    print(f"\nValue counts for column '{col}':")
    print(df[col].value_counts())