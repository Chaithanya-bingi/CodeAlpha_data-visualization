import pandas as pd
import os

# Load dataset
df = pd.read_csv("data/dataset.csv")

# Remove duplicates
df = df.drop_duplicates()

# Create processed folder if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

# Save cleaned dataset
df.to_csv("data/processed/cleaned_dataset.csv", index=False)

print("Data cleaned and saved to data/processed/cleaned_dataset.csv")