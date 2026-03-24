import pandas as pd

# Load dataset
df = pd.read_csv(r"D:\New folder\data_visualization_project\data\dataset.csv")

# Display basic info
print("Dataset loaded successfully!")
print("Shape:", df.shape)
print("Columns:", df.columns)
print(df.head())